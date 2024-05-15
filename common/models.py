from django.contrib.auth import get_user_model
from django.db import models

from books.models import Books

UserModel = get_user_model()


class Likes(models.Model):
    book_to_like = models.ForeignKey(Books, blank=True, on_delete=models.RESTRICT)
    user_who_likes = models.ForeignKey(UserModel, on_delete=models.RESTRICT)
