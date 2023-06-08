from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Receta
from .forms import FormReceta, FormRecetaEditar, FiltrosReceta


class Bienvenida(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        grupos_usuario = user.groups.values_list('name', flat=True)
        context['grupos_usuario'] = grupos_usuario
        return context

class ListRecetas(LoginRequiredMixin, ListView):
    paginate_by = 2
    model = Receta
    extra_context = {'form': FiltrosReceta}

class RecetaDetailView(LoginRequiredMixin, DetailView):
    model = Receta
    template_name = 'recetas/receta_detail.html'

class NuevaReceta(LoginRequiredMixin, CreateView):
    model = Receta
    form_class = FormReceta
    success_url = reverse_lazy('lista_recetas')
    extra_context = {'accion': 'Nueva'}

class EditarReceta(LoginRequiredMixin, UpdateView):
    model = Receta
    form_class = FormRecetaEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_recetas')

class EliminarReceta(LoginRequiredMixin, DeleteView):
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
    return render(request, 'recetas/receta_list.html', context)


def eliminar_todas(request):
    id_list = request.POST.getlist('pk_list[]')

    if id_list:
        for pk in id_list:
            try:
                receta = Receta.objects.get(pk=pk)
                receta.delete()
            except Receta.DoesNotExist:
                pass

    return redirect('lista_recetas')
