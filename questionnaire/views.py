from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
#
# def homepage(request):
#     return HttpResponse("ddd")


def homepage(request):
    l=[]
    return render(request,
                  "qustionnaire/homepage.html",
                  {'a':l})