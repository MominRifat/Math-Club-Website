from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def president(request):
    return render(request, 'formerpresi/presi.html')