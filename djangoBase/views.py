from django.shortcuts import render, HttpResponse
from django.contrib import messages

def home(request):
    messages.success(request, 'Welcome!')
    return render(request, 'index.html')