from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse, reverse
from player.models import Player
from question.models import Question, Answer
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from allauth.socialaccount.models import SocialAccount
from django.utils import timezone

# Create your views here.
@login_required
def getQuestion(request):
    player = get_object_or_404(Player, user=request.user)
    ques = get_object_or_404(Question, level=player.level)
    context = {
        'question': ques,
        'player': player,
        'rank': Player.rank(player),
        'social_account': SocialAccount.objects.get(user=player.user)
    }
    return render(request, "question/index.html", context)

@login_required
@csrf_exempt
def submitAnswer(request):
    player = get_object_or_404(Player, user=request.user)
    ques = get_object_or_404(Question, level=player.level)
    answers = Answer.objects.filter(question=ques)
    status = False 

    for answer in answers:
        if answer.ans == request.POST.get('answer').lower():
            player.level += 1
            player.levelTime = timezone.now()
            player.save()
            status = True
            break

    return HttpResponse(str(status))           