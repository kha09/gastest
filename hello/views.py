from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def log(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "log.html")


def about(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "about.html")