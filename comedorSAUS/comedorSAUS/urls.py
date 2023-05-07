from django.contrib import admin
from django.urls import path, include
from recetario.views import Bienvenida

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Bienvenida.as_view(), name='bienvenida'),
    path('recetario/', include('recetario.urls')),

]
