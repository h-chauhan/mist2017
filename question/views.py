from django.shortcuts import render

# Create your views here.

def get_question(request,lvl):
    player = get_object_or_404(Player, user=request.user)
    ques = get_object_or_404(Question, level=lvl)

    if request.POST.get(level)<=lvl:
        return render(request,"index.html",level)
    else redirect(lvl,permanent=False)