from django.db import models
from django.utils import timezone


class People(models.Model):
    id = models.CharField(max_length=32,primary_key=True)
    reply_channel= models.CharField(max_length=32)
    online=models.IntegerField(null=True)

class ChatList(models.Model):
    id1 = models.CharField(max_length=32)
    id2 = models.CharField(max_length=32)
    id1deleted=models.IntegerField()
    id2deleted=models.IntegerField()

class ChatMessage(models.Model):
    fromid=models.CharField(max_length=32)
    toid=models.CharField(max_length=32)
    text=models.CharField(max_length=128)
    chatlist=models.ForeignKey(ChatList)
    issent=models.IntegerField(null=True)
    time=models.DateTimeField(default=timezone.now)

