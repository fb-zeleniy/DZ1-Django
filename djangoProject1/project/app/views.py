from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def index(request):
    s = "Список объявлений\n\n\n\n\n"
    for b in Bb.objects.all():
        s += b.title + "\n" + b.content + "\n\n\n"
    return HttpResponse(s, content_type="text/plain; charset=utf-8")


def index_html(request):
    return render(request, 'index.html')


def index2(request):
    return HttpResponse("Python Django")


def index3(request):
    return HttpResponse("HomeWork")
