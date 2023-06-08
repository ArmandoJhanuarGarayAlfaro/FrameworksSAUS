from django.conf import settings
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TipoInsumo, Insumo
from .forms import FormTipoInsumo, FiltrosTipoInsumo, FormTipoIngredienteEditar
from .forms import FormInsumo, FiltrosInsumo, FormInsumoEditar
from django_weasyprint import WeasyTemplateResponseMixin

########################### TIPO INSUMO ###########################
class ListTipoInsumos(ListView):
    paginate_by = 2
    model = TipoInsumo
    template_name = 'tipo_insumo/tipo_insumo_list.html'
    extra_context = {'form': FiltrosTipoInsumo}

class NuevoTipoInsumo(CreateView):
    model = TipoInsumo
    form_class = FormTipoInsumo
    template_name = 'tipo_insumo/tipo_insumo_form.html'
    success_url = reverse_lazy('lista_tipo_insumo')
    extra_context = {'accion': 'Nueva'}

class EditarTipoInsumo(UpdateView):
    model = TipoInsumo
    form_class = FormTipoIngredienteEditar
    template_name = 'tipo_insumo/tipo_insumo_form.html'
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_tipo_insumo')

class EliminarTipoInsumo(DeleteView):
    model = TipoInsumo
    template_name = 'tipo_insumo/tipoinsumo_confirm_delete.html'
    success_url = reverse_lazy('lista_tipo_insumo')


def buscar_tipo(request):
    tipo_insumo = TipoInsumo.objects.all().order_by('nombre')

    if request.method == 'POST':

        form = FiltrosTipoInsumo(request.POST)
        nombre = request.POST.get('nombre', None)
        unidad_medida = request.POST.get('unidad_medida', None)

        if nombre:
            tipo_insumo = tipo_insumo.filter(nombre__contains=nombre)
            tipo_insumo = tipo_insumo.filter(nombre__icontains=nombre)
        if unidad_medida:
            tipo_insumo = tipo_insumo.filter(unidad_medida=unidad_medida)

    else:
        form = FiltrosTipoInsumo()

    paginator = Paginator(tipo_insumo, 4)
    page_number = request.POST.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'object_list': page_obj,
        'page_obj': page_obj,
        'form': form
    } 
    return render(request, 'tipo_insumo/tipo_insumo_list.html', context)

def eliminar_tipos(request):
    id_list = request.POST.getlist('pk_list[]')

    if id_list:
        for pk in id_list:
            try:
                tipo_insumo = TipoInsumo.objects.get(pk=pk)
                tipo_insumo.delete()
            except TipoInsumo.DoesNotExist:
                pass

    return redirect('lista_tipo_insumo')

########################### INSUMO ###########################
class ListInsumos(ListView):
    paginate_by = 2
    model = Insumo
    template_name = 'insumo/insumo_list.html'
    extra_context = {'form': FiltrosInsumo}

class NuevoInsumo(CreateView):
    model = Insumo
    form_class = FormInsumo
    template_name = 'insumo/insumo_form.html'
    success_url = reverse_lazy('lista_insumo')
    extra_context = {'accion': 'Nueva'}

class EditarInsumo(UpdateView):
    model = Insumo
    form_class = FormInsumoEditar
    template_name = 'insumo/insumo_form.html'
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_insumo')

class EliminarInsumo(DeleteView):
    model = Insumo
    template_name = 'insumo/insumo_confirm_delete.html'
    success_url = reverse_lazy('lista_insumo')

def buscar_insumo(request):
    insumos = Insumo.objects.all().order_by('nombre')

    if request.method == 'POST':
        form = FiltrosInsumo(request.POST)
        form.is_valid()  # Agregar esta línea para validar el formulario

        nombre = form.cleaned_data.get('nombre')
        codigo = form.cleaned_data.get('codigo')
        cantidad = form.cleaned_data.get('cantidad')
        numero_lote = form.cleaned_data.get('numero_lote')
        proveedor = form.cleaned_data.get('proveedor')
        tipo = form.cleaned_data.get('tipo')

        if nombre:
            insumos = insumos.filter(nombre__icontains=nombre)
        if codigo:
            insumos = insumos.filter(codigo__icontains=codigo)
        if cantidad:
            insumos = insumos.filter(cantidad__icontains=cantidad)
        if numero_lote:
            insumos = insumos.filter(numero_lote__icontains=numero_lote)
        if proveedor:
            insumos = insumos.filter(proveedor__icontains=proveedor)
        if tipo:
            insumos = insumos.filter(tipo=tipo)

    else:
        form = FiltrosInsumo()

    paginator = Paginator(insumos, 4)
    page_number = request.POST.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'object_list': page_obj,
        'page_obj': page_obj,
        'form': form
    } 
    return render(request, 'insumo/insumo_list.html', context)

def buscar_insumo_por_tipo(request, tipo_insumo_id):
    tipo_insumo = TipoInsumo.objects.get(pk=tipo_insumo_id)
    insumos = Insumo.objects.filter(tipo=tipo_insumo)

    paginator = Paginator(insumos, 4)
    page_number = request.POST.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'object_list': page_obj,
        'page_obj': page_obj,
        'form': FiltrosInsumo()  # Se crea una instancia vacía del formulario de filtros
    } 
    return render(request, 'insumo/insumo_list.html', context)


def eliminar_insumos(request):
    id_list = request.POST.getlist('pk_list[]')

    if id_list:
        for pk in id_list:
            try:
                insumo = Insumo.objects.get(pk=pk)
                insumo.delete()
            except Insumo.DoesNotExist:
                pass

    return redirect('lista_insumo')

class VistaPDFInsumos(ListView):
    model = Insumo
    template_name = 'insumo/insumo_pdf.html'

class ListInsumosPdf(WeasyTemplateResponseMixin, VistaPDFInsumos):
    pdf_stylesheets = [
        settings.STATICFILES_DIRS[0] + 'css/bootstrap.min.css',
    ]
    pdf_attachment = False
    pdf_filename = 'insmos.pdf'