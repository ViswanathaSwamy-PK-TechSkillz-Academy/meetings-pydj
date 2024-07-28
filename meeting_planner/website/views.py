from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def welcome(request):
    return render(request, "../templates/website/welcome.html")


def about(request):
    return HttpResponse("I'm  Swamy The Learner !!")


# def welcome(request):
#     return HttpResponse("Welcome to the Meeting Planner!")
