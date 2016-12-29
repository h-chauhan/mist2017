from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from player.models import Player
from django.utils import timezone
import json

# Create your views here.
@csrf_exempt
def createPlayer(request):
    try:
        player = Player.objects.get(fbID=request.POST.get('fbid'))
        player.userToken = request.POST.get('access_token')
        player.save()
    except Player.DoesNotExist:
        player = Player(name=request.POST.get('name'), fbID=request.POST.get('fbid'),
                        userToken=request.POST.get('access_token'), level=1,
                        levelTime=timezone.now(), startTime=timezone.now(), user=request.user)
        player.save()
    return HttpResponse("Success")
