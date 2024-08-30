from django.http import HttpResponse
from .models import Choice
from .models import Question

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def result(request,question_id):

    choice=Choice.objects.get(id=question_id)
    question=Question.objects.get(id=question_id)

    return HttpResponse({question.description," ",choice.choice," ",choice.votes})