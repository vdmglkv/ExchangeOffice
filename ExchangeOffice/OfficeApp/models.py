from django.db import models
from accounts.models import Profile


class Operation(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    currency_in = models.CharField(choices=(('USD', 'USD'), ('EUR', 'EUR'), ('BYN', 'BYN')),
                                   name='From', max_length=3, default='USD')
    value = models.FloatField(default=1)
    currency_out = models.CharField(choices=(('USD', 'USD'), ('EUR', 'EUR'), ('BYN', 'BYN')),
                                    name='To',  max_length=3, default='USD')
    result = models.FloatField(default=1)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user
