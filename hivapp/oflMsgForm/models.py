from django.db import models

# Create your models here.
from django.utils import timezone


class peopleFormid(models.Model):

    openId=models.CharField(max_length=128)
    formId=models.CharField(max_length=128)
    time=models.DateTimeField(default=timezone.now())

class AccessToken(models.Model):
    access_token=models.CharField(max_length=1024)
    time=models.DateTimeField(default=timezone.now())
