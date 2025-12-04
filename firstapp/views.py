from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import datetime

def home(request):
    a=datetime.datetime.now()
    return render(request,'html/index.html',{"time":a})
def good_morning(request):
    return HttpResponse("goood morning")
def good_evening(request):
    return HttpResponse("ggod evening")
def good_night(request):
    return HttpResponse("good night")
