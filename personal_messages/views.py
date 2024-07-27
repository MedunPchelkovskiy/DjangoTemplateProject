from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import redirect, render

from .forms import CreateConversationForm, CreateMessageForm
from .models import Conversations, Messages

UserModel = get_user_model()


def create_conversation(request):
    if request.method == 'GET':
        context = {'form': CreateConversationForm()}
        return render(request, 'create-conversation.html', context)

    participant = UserModel.objects.get(id=request.POST['participant'])
    initiator = request.user

    new_conversation = Conversations(
        participant=participant,
        initiator=initiator,
    )

    new_conversation.save()

    new_message = Messages(
        message_content=request.POST['initial_message'],
        message_to_conversation=new_conversation,
        message_author=request.user
    )

    new_message.save()

    return redirect('my conversations')


def check_for_unread_messages_and_get_owner(filtered_conversations, user):
    for conversation in filtered_conversations:
        messages = Messages.objects.filter(message_to_conversation=conversation.id).all()
        for message in reversed(messages):
            if message.message_unread == True and user != message.message_author:
                conversation.last_unread_message_owner = message.message_author
                conversation.save()
                break
            else:
                break

    return filtered_conversations


def get_my_conversations(request):
    current_user = request.user
    conversations = Conversations.objects.filter(Q(initiator=request.user) | Q(participant=request.user))

    checked_conversations = check_for_unread_messages_and_get_owner(conversations, current_user)

    context = {
        'checked_conversations': checked_conversations,
        'current_user': current_user
    }
    return render(request, 'my-conversations.html', context=context)


def set_message_to_read(curr_conversation, all_messages, user):
    for message in reversed(all_messages):
        if message.message_unread == True and user != message.message_author:
            message.message_unread = False
            curr_conversation.last_unread_message_owner = None
            message.save()
            curr_conversation.save()
        else:
            break
    return all_messages


def read_messages_and_send_new_message(request, pk):
    conversation = Conversations.objects.get(pk=pk)
    messages = Messages.objects.filter(message_to_conversation=pk).all()

    if request.method == 'GET':
        readed_messages = set_message_to_read(conversation, messages, request.user)
        context = {
            'conversation': conversation,
            'readed_messages': readed_messages,
            'message_form': CreateMessageForm()
        }
        return render(request, 'conversation-messages.html', context=context)
    else:
        message_form = CreateMessageForm(request.POST)
        if message_form.is_valid():
            message = message_form.save(commit=False)
            message.message_to_conversation = conversation
            message.message_author = request.user
            message.save()

    return redirect('get messages for conversation', pk=pk)
