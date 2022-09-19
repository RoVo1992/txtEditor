from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class SiteUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User', related_name='siteuser')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        SiteUser.objects.create(user=instance)

