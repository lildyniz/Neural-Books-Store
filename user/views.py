from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth

from store.models import Book
from .forms import UserLoginForm, UserRegistrationForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('store:index'))
    else:
        form = UserLoginForm()

    return render(request, 
                  'user/login.html', 
                  {'form': form},)

def logout(request):
    auth.logout(request)
    return redirect(reverse('store:index'))

def registration(request):

    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('store:index'))
    else:
        form = UserRegistrationForm()
    return render(request, 
                  'user/registration.html', 
                  {'form': form},)

def profile(request):

    books = Book.objects.filter(available=True)
    return render(request, 
                  'user/profile.html', 
                  {'books': books},)