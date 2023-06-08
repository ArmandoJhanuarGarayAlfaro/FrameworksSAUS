from django.urls import path, include
from almacen import views

urlpatterns = [
    # TIPO INSUMO
    path('tipo', views.ListTipoInsumos.as_view(), name='lista_tipo_insumo'),
    path('buscar-tipo', views.buscar_tipo, name='buscar_tipo'),
    path('nuevo-tipo', views.NuevoTipoInsumo.as_view(), name='nuevo_tipo_insumo'),
    path('editar-tipo/<int:pk>', views.EditarTipoInsumo.as_view(), name='editar_tipo_insumo'),
    path('eliminar-tipo/<int:pk>', views.EliminarTipoInsumo.as_view(), name='eliminar_tipo_insumo'),
    path('eliminar-tipos/', views.eliminar_tipos, name='eliminar_tipos'),
    
    # INSUMO
    path('insumo', views.ListInsumos.as_view(), name='lista_insumo'),
    path('buscar-insumo', views.buscar_insumo, name='buscar_insumo'),
    path('nuevo-insumo', views.NuevoInsumo.as_view(), name='nuevo_insumo'),
    path('editar-insumo/<int:pk>', views.EditarInsumo.as_view(), name='editar_insumo'),
    path('eliminar-insumo/<int:pk>', views.EliminarInsumo.as_view(), name='eliminar_insumo'),
    path('eliminar-insumos/', views.eliminar_tipos, name='eliminar_insumos'),
    path('buscar-insumo-por-tipo/<int:tipo_insumo_id>/', views.buscar_insumo_por_tipo, name='buscar_insumo_por_tipo'),
    path('insumo-pdf/', views.ListInsumosPdf.as_view(), name='lista_insumo_pdf'),
]