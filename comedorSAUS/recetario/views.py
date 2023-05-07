from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Receta
from .forms import FormReceta, FormRecetaEditar


class Bienvenida(TemplateView):
    template_name = 'home.html'

class ListRecetas(ListView):
    paginate_by = 5
    model = Receta

class NuevaReceta(CreateView):
    model = Receta
    form_class = FormReceta
    success_url = reverse_lazy('lista_recetas')
    extra_context = {'accion': 'Nueva'}

class EditarReceta(UpdateView):
    model = Receta
    form_class = FormRecetaEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_recetas')

class EliminarReceta(DeleteView):
    model = Receta
    success_url = reverse_lazy('lista_recetas')