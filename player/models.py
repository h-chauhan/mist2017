from django.conf import settings
from django.db import models

# Create your models here.
from django.utils import timezone
class Player(models.Model):
    name = models.CharField(max_length=200) 
    fbID = models.CharField(max_length=200)
    userToken = models.CharField(max_length=200)
    level = models.IntegerField()
    levelTime = models.DateTimeField(default=timezone.now )
    startTime = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL , default = 1)
    def __str__(self):
        return self.name