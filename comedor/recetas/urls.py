from django.urls import path, include
from recetas import views

urlpatterns = [
    path('', views.ListRecetas.as_view(), name='lista_recetas'),
    path('receta/<int:pk>/', views.RecetaDetailView.as_view(), name='receta_detail'),
    path('nueva', views.NuevaReceta.as_view(), name='nueva_receta'),
    path('editar/<int:pk>', views.EditarReceta.as_view(), name='editar_receta'),
    path('eliminar/<int:pk>', views.EliminarReceta.as_view(), name='eliminar_receta'),
    path('buscar-receta', views.buscar_receta, name='buscar_receta'),
    path('eliminar-recetas/', views.eliminar_todas, name='eliminar_todas'),
]