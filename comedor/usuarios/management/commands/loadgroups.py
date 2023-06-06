from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from almacen.models import Insumo, TipoInsumo
from recetas.models import Receta


class Command(BaseCommand):
    help = 'Carga grupos y permisos en la base de datos'

    def handle(self, *args, **options):
        # Crear los grupos
        admin_group, created = Group.objects.get_or_create(name='Administradores')
        if created:
            admin_group.save()

        admin_group, created = Group.objects.get_or_create(name='Chef')
        if created:
            admin_group.save()

        admin_group, created = Group.objects.get_or_create(name='Almacenista')
        if created:
            admin_group.save()

        # Asignar permisos a los grupos
            # Administrador
        admin_group = Group.objects.get(name='Administradores')
        all_permissions = Permission.objects.all()
        admin_group.permissions.set(all_permissions)

            # Chef
        content_type_receta = ContentType.objects.get_for_model(Receta)
        content_type_insumo = ContentType.objects.get_for_model(Insumo)
        content_type_tipo_insumo = ContentType.objects.get_for_model(TipoInsumo)

        permisos_receta = Permission.objects.filter(content_type=content_type_receta)
        permiso_ver_insumo = Permission.objects.get(content_type=content_type_insumo, codename='view_insumo')
        permiso_ver_tipo_insumo = Permission.objects.get(content_type=content_type_tipo_insumo, codename='view_tipoinsumo')

        chef_group = Group.objects.get(name='Chef')
        chef_group.permissions.set(permisos_receta)
        chef_group.permissions.add(*permisos_receta, permiso_ver_insumo, permiso_ver_tipo_insumo)

            # Almacenista
        content_type_tipo_insumo = ContentType.objects.get_for_model(TipoInsumo)
        content_type_insumo = ContentType.objects.get_for_model(Insumo)

        permisos_tipo_insumo = Permission.objects.filter(content_type=content_type_tipo_insumo)
        permisos_insumo = Permission.objects.filter(content_type=content_type_insumo)

        almacenista_group = Group.objects.get(name='Almacenista')
        almacenista_group.permissions.add(*permisos_tipo_insumo, *permisos_insumo)