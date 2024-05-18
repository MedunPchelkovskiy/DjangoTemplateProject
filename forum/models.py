from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

CATEGORY_CHOICES = (
    ("Books", "Books"),
    ("Authors", "Authors"),
    ("Publishers", "Publishers"),
    ("Other", "Other"),
)


class Topics(models.Model):
    topic_name = models.CharField(max_length=100)
    topic_autor = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    topic_creation_date_time = models.DateTimeField(auto_now_add=True)
    posts_count = models.PositiveIntegerField(null=True, blank=True)


class Posts(models.Model):
    text_of_post = models.TextField(max_length=333)
    creation_date_time_of_post = models.DateTimeField(auto_now_add=True)
    editing_date_time_of_post = models.DateTimeField(auto_now_add=True)   # add 'edit post' button in html and forms!!!
    post_to_topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    post_author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
