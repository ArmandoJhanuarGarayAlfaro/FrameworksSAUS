from django.urls import path, include
from recetario import views

urlpatterns = [
    path('', views.ListRecetas.as_view(), name='lista_recetas'),
    path('nueva', views.NuevaReceta.as_view(), name='nueva_receta'),
    path('editar/<int:pk>', views.EditarReceta.as_view(), name='editar_receta'),
    path('eliminar/<int:pk>', views.EliminarReceta.as_view(), name='eliminar_receta'),
    # path('eliminar-receta/', views.eliminar_todas, name='eliminar_todas'),
    # path('buscar-receta', views.buscar_materia, name='buscar_materia'),
]