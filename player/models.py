from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=200) 
    isAdmin = models.BinaryField()
    fbID = models.CharField(max_length=200)
    Email = models.EmailField(max_length=254)
    UserToken = models.CharField(max_length=200)
    level = models.IntegerField()
    timeStamp = models.DateTimeField('date published')
    def __str__(self):
        return self.name