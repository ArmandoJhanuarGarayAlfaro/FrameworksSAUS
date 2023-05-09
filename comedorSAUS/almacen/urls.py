from django.urls import path, include
from almacen import views

urlpatterns = [
    path('', views.ListInsumos.as_view(), name='lista_insumos'),
    path('nuevo', views.NuevoInsumo.as_view(), name='nuevo_insumo'),
    path('editar/<int:pk>', views.EditarInsumo.as_view(), name='editar_insumo'),
    path('eliminar/<int:pk>', views.EliminarInsumo.as_view(), name='eliminar_insumo'),
    path('buscar-insumo', views.buscar_insumo, name='buscar_insumo'),
    # path('eliminar-receta/', views.eliminar_todas, name='eliminar_todas'),
]