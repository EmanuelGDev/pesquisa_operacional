from django.contrib import admin
from django.urls import path, include
from DietaMais.views import principal, resultado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alimentos/', include('DietaMais.urls')),
    path('', principal, name='principal'),
    path('resultado/', resultado ,name='resultado'),
]
