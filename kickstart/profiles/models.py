from django.db import models

from common.models import Common

# Create your models here.
class Profile(Common):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    stripe_account_id = models.CharField(max_length=255, blank=True, null=True)
