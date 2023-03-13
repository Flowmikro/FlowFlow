from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('action/', views.action, name='action'),
    path('reg/', views.reg, name='reg'),
    path('buy_porsche/', views.buy_porsche, name='buy_porsche')

]