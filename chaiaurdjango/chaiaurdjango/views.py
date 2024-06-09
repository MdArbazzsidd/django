from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("hey you are in now home page ")

def officalpage(request):
    return render(request,'index.html')