"""RegistroDeAlumnos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
#from django.contrib import admin
from django.urls import path

from Models.Producto.views import FormularioProductoView, FormularioMarcaView, FormularioCategoriaView
from Views.HomeView import HomeView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("", HomeView.home, name="home"),
    path("registrarProducto/", FormularioProductoView.index, name="registrarProducto"),
    path("registrarMarca/", FormularioMarcaView.index, name="registrarMarca"),
    path("registrarCategoria/", FormularioCategoriaView.index, name="registrarCategoria"),
    path("guardarProducto/", FormularioProductoView.procesar_formulario, name="guardarProducto"),
    path("listarProductos/", FormularioProductoView.listar_productos, name="listarProductos"),
    path("listarMarca/", FormularioProductoView.listar_marca, name="listarMarca"),
    path("listarCategoria", FormularioProductoView.listar_categoria, name="listarCategoria"),
    path("editarProductos/<int:id_producto>", FormularioProductoView.edit, name="editarProductos"),
    path("actualizarProductos/<int:id_producto>", FormularioProductoView.actualizar_producto, name="actualizarProductos"),
    path("eliminarProductos/<int:id_producto>", FormularioProductoView.delete, name="eliminarProductos"),
]
