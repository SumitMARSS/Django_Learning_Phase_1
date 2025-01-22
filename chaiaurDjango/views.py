from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello jii: This is my home page")
    return render(request, 'websites/home.html')

def about(request):
    # return HttpResponse("Hello jii: This is my about page")
    return render(request, 'index.html')

def contact(request):
    return HttpResponse("Hello jii: This is my contact page")
