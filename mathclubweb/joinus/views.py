from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def joinus(request):
    return render(request, 'joinus/join.html')