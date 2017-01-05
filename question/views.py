from django.shortcuts import render

# Create your views here.

def get_question(request,lvl):
    player = get_object_or_404(Player, user=request.user)
    ques = get_object_or_404(Question, level=lvl)

    if request.POST.get(level)<=lvl:
        return render(request,"index.html",level)
    else redirect(lvl,permanent=False)

def submitAnswer(request,lvl):
    ques = get_object_or_404(Question, level=lvl)
    player = get_object_or_404(Player, user=request.user)
    answers = Answer.objects.filter(question=ques)
    status = False 

    for answer in answers:
        if answer.ans == lower(request.POST.get('answer')):
            player.level += 1
            player.save()
            status = True
            break

    return HttpResponse(status)           