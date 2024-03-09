from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch

from store.models import Book
from cart.models import Cart
from orders.models import Order, OrderItem
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, вы успешно вошли в аккаунт!")
                
                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
                
                return HttpResponseRedirect(reverse('store:index'))
    else:
        form = UserLoginForm()

    return render(request, 
                  'user/login.html', 
                  {'form': form},)

@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, вы вышли из аккаунта.")
    auth.logout(request)
    return redirect(reverse('store:index'))

def registration(request):

    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

            messages.success(request, f"{user.username}, вы успешно зарегистрировались!")
            return HttpResponseRedirect(reverse('store:index'))
    else:
        form = UserRegistrationForm()
    return render(request, 
                  'user/registration.html', 
                  {'form': form},)

@login_required
def profile(request):

    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль успешно обновлен!")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    orders = Order.objects.filter(user=request.user).prefetch_related(
                Prefetch(
                    "orderitem_set",
                    queryset=OrderItem.objects.select_related("product"),
                )
            ).order_by("-id")
    
    return render(request, 
                  'user/profile.html', 
                  {'form': form,
                   'orders': orders},)

def cart(request):
    return render(request, 'user/cart.html')