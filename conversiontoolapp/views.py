from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    context = {}  # Create an empty context dictionary
    return render(request, 'login.html', context)

def convertor(request):
    context = {}  # Create an empty context dictionary
    return render(request, 'convertor.html', context)
