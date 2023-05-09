from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Insumo
from .forms import FormInsumo, FormInsumoEditar, FiltrosInsumo


class Bienvenida(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

class ListInsumos(LoginRequiredMixin, ListView):
    paginate_by = 2
    model = Insumo
    extra_context = {'form': FiltrosInsumo}

class NuevoInsumo(LoginRequiredMixin, CreateView):
    model = Insumo
    form_class = FormInsumo
    success_url = reverse_lazy('lista_insumos')
    extra_context = {'accion': 'Nueva'}

class EditarInsumo(LoginRequiredMixin, UpdateView):
    model = Insumo
    form_class = FormInsumoEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_insumos')

class EliminarInsumo(LoginRequiredMixin, DeleteView):
    model = Insumo
    success_url = reverse_lazy('lista_insumos')

def buscar_insumo(LoginRequiredMixin, request):
    insumos = Insumo.objects.all().order_by('nombre')

    if request.method == 'POST':

        form = FiltrosInsumo(request.POST)
        nombre = request.POST.get('nombre', None)

        if nombre:
            insumos = insumos.filter(nombre__contains=nombre)
            insumos = insumos.filter(nombre__icontains=nombre)

    else:
        form = FiltrosInsumo()

    paginator = Paginator(insumos, 2)  # Show 25 contacts per page.
    page_number = request.POST.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'object_list': page_obj,
        'page_obj': page_obj,
        'form': form
    } 
    return render(request, 'almacen/insumo_list.html', context)
