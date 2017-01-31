from django.conf import settings
from django.db import models
from django.db.models import Q

# Create your models here.
from django.utils import timezone
class Player(models.Model):
    level = models.IntegerField()
    levelTime = models.DateTimeField(default=timezone.now )
    startTime = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL , default = 1)

    def rank(player):
        playerlist = Player.objects.filter(user__is_staff=False).filter(((Q(level__gt=player.level)) | (Q(level=player.level)) & Q(levelTime__lt=player.levelTime)))  
        return len(playerlist) + 1

    def __str__(self):
        return self.user.first_name

class Submission(models.Model):
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    question = models.ForeignKey('question.Question', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    ans = models.CharField(max_length=200)