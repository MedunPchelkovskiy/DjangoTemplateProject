from django.dispatch import receiver
from django.db.models import signals
from accounts_manage.models import LibraryUser, UserProfile
from django.contrib.auth import get_user_model

UserModel = get_user_model()

@receiver(signals.post_save, sender=UserModel)
def create_profile_when_create_user(instance, created, *args, **kwargs):
    if created:
        UserProfile.objects.create(
            user_id = instance.pk
        )
    else:
        return