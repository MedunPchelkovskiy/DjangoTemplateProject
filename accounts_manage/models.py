from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MinLengthValidator

from accounts_manage.managers import LibraryUserManager


# UserModel = get_user_model()


class LibraryUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2)],
        unique=True,
        null=False,
        blank=False)

    date_joined = models.DateTimeField(auto_now_add=True)

    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'  # change 'USERNAME_FIELD' to be 'email' and add functionality: - e-mail notification when someone add book from your preferred genre or put mail like option in profile and choose to receive these notifications!!

    objects = LibraryUserManager()

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    first_name = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(2)],
        null=True,
        blank=True
    )
    last_name = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(2)],
        null=True,
        blank=True
    )
    age = models.PositiveBigIntegerField(
        null=True,
        blank=True
    )

    user = models.OneToOneField(
        LibraryUser,
        primary_key=True,
        on_delete=models.CASCADE
    )
