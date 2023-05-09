# Generated by Django 4.1.6 on 2023-05-09 03:21

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfc', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(code='rfc_invalido', message='El RFC no tiene un formato válido', regex='^([A-ZÑ&]{3,4}) ?(?:- ?)?(\\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\\d|3[01])) ?(?:- ?)?([A-Z\\d]{2})([A\\d])$')], verbose_name='R.F.C.')),
                ('nombre', models.CharField(max_length=150)),
                ('apellido_paterno', models.CharField(max_length=150)),
                ('apellido_materno', models.CharField(max_length=150)),
                ('avatar', models.ImageField(upload_to='perfiles', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'], message='Sólo se permiten imágenes PNG, JPG o JPEG')], verbose_name='Foto de perfil')),
                ('fecha_nacimiento', models.DateField()),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
    ]