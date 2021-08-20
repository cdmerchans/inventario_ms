"""inventarioProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventarioApp.views import AgregarProducto, VerProductos, BuscarProducto, ActualizarCantidad
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('producto/', csrf_exempt(AgregarProducto.as_view())),
    path('carta/', csrf_exempt(VerProductos.as_view())),
    path('buscar/', csrf_exempt(BuscarProducto.as_view())),
    path('cantidad/', csrf_exempt(ActualizarCantidad.as_view())),
]
