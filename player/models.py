from django.conf import settings
from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=200) 
    isAdmin = models.BinaryField()
    fbID = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    userToken = models.CharField(max_length=200)
    level = models.IntegerField()
    timeStamp = models.DateTimeField('date published')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    def __str__(self):
        return self.name