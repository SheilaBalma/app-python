from django.contrib import admin
from django.urls import path
from clima.views import BuscarCiudadView, PronosticoView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", BuscarCiudadView.as_view(), name="home"),
    path("pronostico/", PronosticoView.as_view(), name="pronostico"),
]