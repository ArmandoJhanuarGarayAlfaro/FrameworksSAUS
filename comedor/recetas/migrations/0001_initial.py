# Generated by Django 4.1.6 on 2023-06-02 05:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('descripcion', models.CharField(max_length=1000)),
                ('hora', models.SmallIntegerField(verbose_name='Hora(s)')),
                ('minuto', models.SmallIntegerField(verbose_name='Minuto(s)')),
                ('ingredientes', models.TextField(blank=True, null=True)),
                ('instrucciones', models.TextField(blank=True, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='img_recetas', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'], message='Sólo se permiten imágenes PNG, JPG o JPEG')], verbose_name='Foto de platillo')),
            ],
        ),
    ]