from .models import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
User = get_user_model()

@receiver(post_save, sender=User)
def user_create_handler(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(
            user=instance,
            first_name=instance.first_name,
            last_name=instance.last_name
        )
        profile.save()

