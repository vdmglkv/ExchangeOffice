from django.db import models
from accounts.models import Profile


class Operation(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    currency_in = models.CharField(max_length=10)
    currency_out = models.CharField(max_length=10)
    value_in = models.DecimalField(max_digits=19, decimal_places=10)
    value_out = models.DecimalField(max_digits=19, decimal_places=10)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user
