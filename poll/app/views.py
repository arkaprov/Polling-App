from django.http import HttpResponse
from .models import Choice
from .models import Question
from django.shortcuts import render
from .forms import VoteFrom

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request,question_id):
    question=Question.objects.get(id=question_id)
    return HttpResponse(question.description)

def form(request,question_id):
    if request.method=='POST':
        choice=request.POST.get('choice')
        choice_obj=Choice.objects.get(id=choice)
        choice_obj.votes+=1
        choice_obj.save()
        return HttpResponse("Votes casted successfully")
    form_data=VoteFrom(question_id)
    context={"form": form_data}
    return render(request,"vote.html",context)

#Display the result
def result(request,question_id):
    question = Question.objects.get(id=question_id)
    choice_list=Choice.objects.filter(question=question_id)
    context={
        "question_description":question.description,
        "question_choices":choice_list
    }
    return render(request,"result.html",context)

