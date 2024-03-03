from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.book_list, name='search'),
    path('list/<slug:slug>/', views.book_list,
        name='book_list'),
    path('<int:id>/<slug:slug>/', views.book_detail,
         name='book_detail'),
]