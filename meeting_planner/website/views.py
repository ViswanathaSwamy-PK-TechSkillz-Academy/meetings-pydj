from django.http import HttpResponse
from django.shortcuts import render

from meetings.models import Meeting


# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html",
                  {"meetings": Meeting.objects.all()})


def about(request):
    return HttpResponse("I'm  Swamy The Learner !!")


# def welcome(request):
#     return HttpResponse("Welcome to the Meeting Planner!")
