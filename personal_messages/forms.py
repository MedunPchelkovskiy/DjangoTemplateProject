from django import forms

from .models import Conversations, Messages


class CreateConversationForm(forms.ModelForm):
    initial_message = forms.CharField(max_length=333)

    class Meta:
        model = Conversations
        fields = ['participant', ]
        labels = {
            'participant': 'Participant:',
        }


class CreateMessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['message_content']
        labels = {
            'message_content': 'Write message:',
        }
        widgets = {
            'message_content': forms.TextInput(attrs={'placeholder': 'Write message'}),
        }
