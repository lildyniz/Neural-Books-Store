from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('cart/', views.cart, name='cart'),

    path('favorite_list/', views.favorite_list, name='favorite_list'),
    path('favorite_add/', views.favorite_add, name='favorite_add'),
    path('favorite_remove/', views.favorite_remove, name='favorite_remove'),
]