from django.urls import path
from usuarios.views import Login, ListaUsuarios, eliminar_usuario, asignar_grupos, nuevo_usuario, buscar_usuario, logout_view, editar_usuario, eliminar_usuarios

urlpatterns = [
    path('', Login.as_view(), name="login"),
    path('logout/', logout_view, name='logout'),
    path('lista/', ListaUsuarios.as_view(), name='lista_usuarios'),
    path('nuevo-usuario/', nuevo_usuario, name='nuevo_usuario'),
    path('buscar-usuario/', buscar_usuario, name='buscar_usuario'),
    path('editar_usuario/<int:pk>/', editar_usuario, name='editar_usuario'),
    path('eliminar-usuario/<int:pk>/', eliminar_usuario, name='eliminar_usuario'),
    path('eliminar_usuarios/', eliminar_usuarios, name='eliminar_usuarios'),
    path('asignar-grupos/', asignar_grupos, name='asignar_grupos'),
    # path('eliminar_usuario/<int:pk>',views.EliminarUsuario.as_view(),name='eliminar_usuario'),
]                                                                    