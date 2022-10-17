from django.shortcuts import render, HttpResponse
from django.contrib import messages

def signUp(request):
    # messages.info(request, 'Done')
    return render(request, 'user/signUp.html')

def signIn(request):
    # messages.info(request, 'Done')
    return render(request, 'user/signIn.html')
