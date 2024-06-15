from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def index(request) -> HttpResponse:
    context = {
        "title": 'Online Organizer',
    }
    return render(request, 'main/index.html', context)
