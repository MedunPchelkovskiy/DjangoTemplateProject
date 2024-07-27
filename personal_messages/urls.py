from django.urls import path

from .views import get_my_conversations, create_conversation, read_messages_and_send_new_message

urlpatterns = [
    path('my-conversations/', get_my_conversations, name='my conversations'),
    path('create/', create_conversation, name='create conversation'),
    path('conversation-messages/<int:pk>/', read_messages_and_send_new_message, name='get messages for conversation'),

]
