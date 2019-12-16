from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'HTML/project1.html')


def registration(request):
    return render(request, 'HTML/registration.html')
