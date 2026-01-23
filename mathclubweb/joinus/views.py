from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def joinus(request):
    return HttpResponse("This is the join us page.")