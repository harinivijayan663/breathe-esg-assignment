from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sap/', views.sap, name='sap'),
    path('utility/', views.utility, name='utility'),
    path('travel/', views.travel, name='travel'),
]