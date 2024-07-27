from django.contrib import admin

from .models import Conversations, Messages


@admin.register(Conversations)
class ConversationsAdmin(admin.ModelAdmin):
    list_display = ('initiator', 'participant', )


@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ('message_content', 'message_date_time', 'message_author','message_to_conversation', 'message_unread',)