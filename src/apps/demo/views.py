from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("You are now running a stack with django, postgres, nginx, and gunicorn")
