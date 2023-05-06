from django.views.generic import TemplateView
from django.shortcuts import render

class Bienvenida(TemplateView):
    template_name = 'home.html'