from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def resource(request):
    return HttpResponse("This is the resource page.")