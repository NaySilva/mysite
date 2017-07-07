from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from polls.models import Question

def index(request):
    questions = Question.objects.all()
    return render(request, 'index.html', {'questions':questions})

def exibir(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'question.html', {'question': question})