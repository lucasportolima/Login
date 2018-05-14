from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    titulo = "creuzin"
    return render(request, 'index.html', {
        'titulo' : titulo,
    })
