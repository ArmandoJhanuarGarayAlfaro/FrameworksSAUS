import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'comedorSAUS.settings')
django.setup()


from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType

from usuarios.models import Usuario



grupo_administradores = Group.objects.create(name='administradores')

grupo_chefs = Group.objects.create(name='chefs')

content_type = ContentType.objects.get_for_model(Usuario)

permiso_chefs = Permission.objects.create(
    codename = 'permiso_chef',
    name = 'Permiso requerido para el grupo chefs',
    content_type = content_type
)

permiso_administradores = Permission.objects.create(
    codename = 'permiso_administradores',
    name = 'Permiso requerido para el grupo administradores',
    content_type = content_type
)

grupo_chefs.permissions.add(permiso_chefs)
grupo_administradores.permissions.add(permiso_administradores)


administrador = Usuario.objects.create_user('admin@admin.mx', password='admin123')
administrador.groups.add(grupo_administradores)

Usuario.objects.create_superuser('chef@chef.mx', password='chef123')