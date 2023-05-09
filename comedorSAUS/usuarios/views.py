from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .token import token_activacion
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.views.generic import TemplateView

from .forms import UserForm
from .models import Chef



class LoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    

class RegistroChef(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'registrar_chef.html'
    form_class = UserForm
    success_message = '%(username)s se registró con éxito'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form = UserForm(self.request.POST)
        if form.is_valid():
            # grupo = Group.objects.get(name='chefs')
            user = form.save(commit=False)
            user.is_active = True
            # user.groups.add(grupo)
            user.save()
            dominio = get_current_site(self.request)
            mensaje = render_to_string('confirmar_cuenta.html',
                                       {
                                           'user': user,
                                           'dominio': dominio,
                                           'uid': urlsafe_base64_encode(force_bytes(user.id)),
                                           'token': token_activacion.make_token(user)
                                       }
                                       )

            email = EmailMessage(
                'Activar cuenta ',
                mensaje,
                to=[user.email]
            )
            email.content_subtype = "html"
            email.send()
        else:
            return self.render_to_response(self.get_context_data(form=form))
        return super().form_valid(form)

class ActivarCuenta(TemplateView):
    

    def get(self, request, *args, **kwargs):

        try:
            uid = urlsafe_base64_decode(kwargs['uidb64'])
            token = kwargs['token']
            user = User.objects.get(pk=uid) 
        except(TypeError, ValueError, User.DoesNotExist):
            user = None
        
        if user is not None and token_activacion.check_token(user, token):
            user.is_active = True
            user.save()
            mensaje = 'Cuenta activada, ingresar datos'
        else:
            mensaje = 'Token inválido, contacta al administrador'

        return render(request, 'login.html', {'mensaje':mensaje})