from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    balance = models.JSONField(default={'USD': 1000, 'EUR': 1000, 'BYN': 1000})

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
