from django.urls import path
from . import views

urlpatterns = [
    path(r'main/', views.main, name='main'),
    path(r'detail/', views.detail, name='detail'),
    path(r'add/', views.add, name="add")
]