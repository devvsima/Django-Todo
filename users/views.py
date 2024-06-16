from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import LoginForm, SignUpForm
from django.http import HttpResponseRedirect

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:index')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

# Create your views here.
def index(request):
    context = {
        "title": 'Online Organizer',
    }
    return render(request, 'users/index.html', context)

@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))