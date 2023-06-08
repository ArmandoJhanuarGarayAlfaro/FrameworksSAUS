from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

class FormUsuario(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Username'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Contraseña'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Confirmar contraseña'})
    )
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Nombre'}),
        required=False
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Apellido'}),
        required=False
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Email'}),
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()

            # Envío de correo de confirmación
            subject = 'Confirmación de registro'
            message = 'Gracias por registrarte. Tu cuenta ha sido creada exitosamente.'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = self.cleaned_data['email']
            send_mail(subject, message, from_email, [to_email])

        return user


class FiltrosUsuario(FormUsuario):

    def __init__(self, *args, **kwargs):
        super(FiltrosUsuario, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].required = False
