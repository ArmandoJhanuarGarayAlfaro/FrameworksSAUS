
from django.contrib import admin
from django.urls import path, include
from recetas.views import Bienvenida
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

# METHODS
# GET POST PUT PATCH DELETE

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Bienvenida.as_view(),name='bienvenida'),
    path('recetas/', include('recetas.urls')),
    path('almacen/', include('almacen.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
