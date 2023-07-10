from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def port(request):
    return render(request,"port.html")

def home(request):
    return render(request,"other/home.html")
def about(request):
    return render(request,"other/about.html")
def projects(request):
    return render(request,"other/projects.html")
def contact(request):
    return render(request,"other/contact.html")