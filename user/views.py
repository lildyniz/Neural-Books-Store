from django.shortcuts import render, get_object_or_404
from store.models import Book

def login(request):

    return render(request, 
                  'user/login.html', 
                  {},)

def logout(request):
    
    return render(request, 
                  '', 
                  {},)

def registration(request):
    
    return render(request, 
                  'user/registration.html', 
                  {},)

def profile(request):

    books = Book.objects.filter(available=True)
    return render(request, 
                  'user/profile.html', 
                  {'books': books},)