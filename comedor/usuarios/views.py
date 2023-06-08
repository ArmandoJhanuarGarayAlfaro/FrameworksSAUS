from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth import logout
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from .forms import FormUsuario, FiltrosUsuario


class Login(LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm

def logout_view(request):
    logout(request)
    return redirect('login')

class ListaUsuarios(LoginRequiredMixin, PermissionRequiredMixin,ListView):
    permission_required = 'auth.view_user'
    raise_exception = True
    model = User
    paginate_by = 2
    template_name = 'usuarios_list.html'
    extra_context = {'form': FiltrosUsuario}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grupos'] = Group.objects.all()
        return context

@permission_required('auth.add_user')
def nuevo_usuario(request):
    if request.method == 'POST':
        form = FormUsuario(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'El usuario se guardó correctamente.')
            return redirect('lista_usuarios')
        else:
            messages.error(request, 'Hubo errores en el formulario. Por favor, corrígelos.')
    else:
        form = FormUsuario()
    return render(request, 'usuario_form.html', {'form': form})

@permission_required('auth.change_user')
def editar_usuario(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        form = FormUsuario(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'El usuario se actualizó correctamente.')
            return redirect('lista_usuarios')
        else:
            messages.error(request, 'Hubo errores en el formulario. Por favor, corrígelos.')
    else:
        form = FormUsuario(instance=user)

    return render(request, 'usuario_form.html', {'form': form})

@permission_required('auth.delete_user')
def eliminar_usuario(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        user.delete()
        messages.success(request, 'El usuario se eliminó correctamente.')
        return redirect('lista_usuarios')

    return render(request, 'eliminar_usuario.html', {'user': user})

@permission_required('auth.view_user')
def buscar_usuario(request):
    users = User.objects.all().order_by('username')

    if request.method == 'POST':
        form = FiltrosUsuario(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')

            if username:
                users = users.filter(username__icontains=username)
            if password:
                users = users.filter(password__icontains=password)
            if first_name:
                users = users.filter(first_name__icontains=first_name)
            if last_name:
                users = users.filter(last_name__icontains=last_name)
            if email:
                users = users.filter(email__icontains=email)

    else:
        form = FiltrosUsuario()

    paginator = Paginator(users, 2)
    page_number = request.POST.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'object_list': page_obj,
        'page_obj': page_obj,
        'form': form
    }
    return render(request, 'usuarios_list.html', context)

@permission_required('auth.delete_user')
def eliminar_usuarios(request):
    User = get_user_model()
    id_list = request.POST.getlist('pk_list[]')

    if id_list:
        for pk in id_list:
            try:
                user = User.objects.get(pk=pk)
                user.delete()
            except User.DoesNotExist:
                pass

    messages.success(request, 'Los usuarios seleccionados se eliminaron correctamente.')
    return redirect('lista_usuarios')

@permission_required('auth.change_user')
def asignar_grupos(request):
    if request.method == 'POST':
        user_ids = request.POST.getlist('pk_list[]')
        group_id = request.POST.get('grupo')

        group = Group.objects.get(id=group_id)
        users = User.objects.filter(id__in=user_ids)

        for user in users:
            # Eliminar grupo previo, si existe
            user.groups.clear()
            # Asignar nuevo grupo
            user.groups.add(group)

        messages.success(request, 'Se asignaron los grupos correctamente a los usuarios seleccionados.')
        return redirect('lista_usuarios')

    users = User.objects.all()
    grupos = Group.objects.all()
    return render(request, 'usuarios_list.html', {'users': users, 'grupos': grupos})

