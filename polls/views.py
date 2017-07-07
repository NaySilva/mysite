from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from polls.models import Question, Choice


def index(request):
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'index.html', {'questions':questions})

def exibir(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = Choice.objects.filter(question=question)
    return render(request, 'question.html', {'question': question, 'choices':choices})

def result(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = Choice.objects.filter(question=question)
    return render(request, 'result.html', {'question': question, 'choices':choices})

def vote(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = Choice.objects.filter(question=question)
    return render(request, 'votar.html', {'question': question, 'choices':choices})

def votar(request, choice_id):
    choice = Choice.objects.get(id=choice_id)
    choice.votes += 1
    choice.save(force_update=True)
    return redirect('index')

def remove(request, choice_id):
    choice = Choice.objects.get(id=choice_id)
    choice.delete()
    return redirect('index')

def mudar_status(request, question_id):
    question = Question.objects.get(id=question_id)
    question.closed = not question.closed
    question.save(force_update=True)
    return redirect('index')

def manage(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = Choice.objects.filter(question=question)
    return render(request, 'manage.html', {'question': question, 'choices': choices})
