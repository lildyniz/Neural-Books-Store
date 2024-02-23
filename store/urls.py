from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.book_list, name='book_list'),
    path('list/<slug:slug>/', views.book_list,
        name='book_list_by_category'),
    path('<int:id>/<slug:slug>/', views.book_detail,
         name='book_detail'),
]