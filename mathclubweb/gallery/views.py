from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def gallery(request):
    return HttpResponse("This is the gallery page.")