from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def event(request):
    return render(request, 'event/event.html')