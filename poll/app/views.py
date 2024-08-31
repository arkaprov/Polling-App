from django.http import HttpResponse
from .models import Choice
from .models import Question

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def detail(request,question_id):
    question=Question.objects.get(id=question_id)
    return HttpResponse(question.description)
#Display the result
def result(request,question_id):
    question = Question.objects.get(id=question_id)
    choice_list=Choice.objects.filter(question=question_id)
    choice_str="".join([f"{choice.choice} {choice.votes} <br>"for choice in choice_list])


    return HttpResponse({f"{question.description}<br>{choice_str}"})