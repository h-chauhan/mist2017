from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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

def getPlayer(request):
    player = get_object_or_404(Player, user=request.user)
    s=serialzers.serialize('json', [player])
    return HttpResponse(s,content_type="application/json")

def playerList(request):
    player_list = Player.objects.order_by('-level', 'levelTime', 'pk')
    paginator = Paginator(player_list, 25) # Show 25 player per page

    page = request.GET.get('page')
    try:
        player = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        player = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        player = paginator.page(paginator.num_pages)

    return render(request, 'list.html', {'players': player})

def rank(player):
    playerlist = Player.objects.filter(((Q(level__gt=player.level)) | (Q(level=player.level)) & Q(levelTime__lt=player.levelTime)))  
    return len(playerlist + 1)

