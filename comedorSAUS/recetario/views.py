from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from .models import Receta
from .forms import FormReceta, FormRecetaEditar, FiltrosReceta


class Bienvenida(TemplateView):
    template_name = 'home.html'

class ListRecetas(ListView):
    paginate_by = 2
    model = Receta
    extra_context = {'form': FiltrosReceta}


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


def buscar_receta(request):
    recetas = Receta.objects.all().order_by('nombre')

    if request.method == 'POST':

        form = FiltrosReceta(request.POST)
        nombre = request.POST.get('nombre', None)
        hora = request.POST.get('hora', None)
        minuto = request.POST.get('minuto', None)

        if nombre:
            recetas = recetas.filter(nombre__contains=nombre)
            recetas = recetas.filter(nombre__icontains=nombre)
        if hora:
            recetas = recetas.filter(hora=hora)
        if minuto:
            recetas = recetas.filter(minuto=minuto)

    else:
        form = FiltrosReceta()

    paginator = Paginator(recetas, 2)  # Show 25 contacts per page.
    page_number = request.POST.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'object_list': page_obj,
        'page_obj': page_obj,
        'form': form
    } 
    return render(request, 'recetario/receta_list.html', context)
