from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner!")


def about(request):
    return HttpResponse("I'm  Swamy The Learner !!")
