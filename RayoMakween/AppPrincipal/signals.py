from .models import User
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def assign_default_error(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='Cliente')
        instance.groups.add(group)