from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def president(request):
    return HttpResponse("This is the former presidents page.")