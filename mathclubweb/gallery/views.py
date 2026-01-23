from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def gallary(request):
    return HttpResponse("This is the gallery page.")