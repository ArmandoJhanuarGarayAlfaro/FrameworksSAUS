from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('nuevo_chef/', views.RegistroChef.as_view(), name='nuevo_chef'),
    path('activar/<slug:uidb64>/<slug:token>', views.ActivarCuenta.as_view(), name='activar'),

]