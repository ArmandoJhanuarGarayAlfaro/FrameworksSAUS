# Generated by Django 4.1.6 on 2023-06-02 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoInsumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('unidad_medida', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=20, unique=True)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('numero_lote', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_caducidad', models.DateField(blank=True, null=True)),
                ('proveedor', models.CharField(max_length=100)),
                ('tipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='insumos', to='almacen.tipoinsumo')),
            ],
        ),
    ]