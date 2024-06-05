from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Conversations(models.Model):
    initiator = models.ForeignKey(UserModel, related_name='initiator', null=False, blank=True, on_delete=models.RESTRICT)
    participant = models.ForeignKey(UserModel, related_name='participant', null=False, blank=False, on_delete=models.RESTRICT)
    last_unread_message_owner = models.ForeignKey(UserModel, null=True, blank=True, on_delete=models.RESTRICT)


class Messages(models.Model):
    message_content = models.TextField(max_length=333)
    message_date_time = models.DateTimeField(auto_now_add=True)
    message_author = models.ForeignKey(UserModel, null=False, blank=True, on_delete=models.RESTRICT)
    message_to_conversation = models.ForeignKey(Conversations, on_delete=models.CASCADE)
    message_unread = models.BooleanField(default=True)
