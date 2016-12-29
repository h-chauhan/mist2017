from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from player.models import Player
from django.utils import timezone
import json

# Create your views here.
@csrf_exempt
def createPlayer(request):
    body = json.loads(request.body.decode("utf-8"))
    try:
        body['fbid']
        print(str(body['fbid']))
        player = Player.objects.get(fbID=str(body['fbid']))
        player.userToken = body['access_token']
        player.save()
    except Player.DoesNotExist:
        player = Player(name=body['name'], fbID=body['fbid'],
                        userToken=body['access_token'], level=1,
                        levelTime=timezone.now, startTime=timezone.now, user=request.user)
        player.save()
        print()
    return HttpResponse("Success")
