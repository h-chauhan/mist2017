from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse
from player.models import Player
from question.models import Question, Answer
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def getQuestion(request, lvl):
    player = get_object_or_404(Player, user=request.user)
    ques = get_object_or_404(Question, level=lvl)

    if int(lvl) <= player.level:
        context = {
            'question': ques,
            'player': player,
            'rank': Player.rank(player),
        }
        return render(request, "question/index.html", context)
    else:
        HttpResponseRedirect(reverse('question', args=(player.level)))

@login_required
def submitAnswer(request, lvl):
    ques = get_object_or_404(Question, level=lvl)
    player = get_object_or_404(Player, user=request.user)
    answers = Answer.objects.filter(question=ques)
    status = False 

    for answer in answers:
        if answer.ans == request.POST.get('answer').lower():
            player.level += 1
            player.save()
            status = True
            break

    return HttpResponse(str(status))           