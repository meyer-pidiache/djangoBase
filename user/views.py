from django.shortcuts import render, HttpResponse
from django.contrib import messages

def register(request):
    messages.info(request, 'Done')
    return render(request, 'user/register.html')
