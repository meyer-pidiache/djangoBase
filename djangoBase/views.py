from django.shortcuts import render

def cover(request):
    return render(request, 'index.html')
