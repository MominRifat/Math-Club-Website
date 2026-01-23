from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def panel(request):
    return HttpResponse("This is the panel page.")