from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, "appearance/index.html")
def greet(request , name):
    return HttpResponse(f"Hello, {name}. You're at the gallery greet.")
def about(request):
    return render(request, "appearance/about.html")

# Create your views here.