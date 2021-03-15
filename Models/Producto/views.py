from django.http import HttpRequest
from django.shortcuts import render

from Models.Producto.forms import FormularioProducto
from Models.Producto.forms import FormularioMarca
from Models.Producto.forms import FormularioCategoria
from Models.Producto.models import Producto
from Models.Producto.models import Marca
from Models.Producto.models import Categoria


class FormularioProductoView(HttpRequest):

    def index(request):
        producto = FormularioProducto()
        return render(request, "ProductoIndex.html", {"form": producto})

    def procesar_formulario(request):
        producto = FormularioProducto(request.POST)
        if producto.is_valid():
            producto.save()
            producto = FormularioProducto()
        return render(request, "ProductoIndex.html", {"form": producto, "mensaje": "ok"})

    def listar_productos(request):
        productos = Producto.objects.all()
        return render(request, "ListaProducto.html", {"productos": productos})

    def listar_marca(request):
        productos = Producto.objects.all()
        return render(request, "ListaMarca.html", {"productos": productos})

    def listar_categoria(request):
        productos = Producto.objects.all()
        return render(request, "ListaCategoria.html", {"productos": productos})

    def edit(request, id_producto):
        producto = Producto.objects.filter(id=id_producto).first()
        form = FormularioProducto(instance=producto)
        return render(request, "ProductoEdit.html", {"form": form, "producto": producto})

    def actualizar_producto(request, id_producto):
        producto = Producto.objects.get(pk=id_producto)
        form = FormularioProducto(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        productos = Producto.objects.all()
        return render(request, "ListaCategoria.html", {"productos": productos})

    def delete(request, id_producto):
        producto = Producto.objects.get(pk=id_producto)
        producto.delete()
        productos = Producto.objects.all()
        return render(request, "ListaCategoria.html", {"productos": productos, "mensaje": "ok"})

class FormularioMarcaView(HttpRequest):

    def index(request):
        marca = FormularioMarca()
        return render(request, "MarcaIndex.html", {"form": marca})

    def procesar_formulario(request):
        marca = FormularioMarca(request.POST)
        if marca.is_valid():
            marca.save()
            marca = FormularioMarca()
        return render(request, "MarcaIndex.html", {"form": marca, "mensaje": "ok"})

    def listar_productos(request):
        productos = Producto.objects.all()
        return render(request, "ListaProducto.html", {"productos": productos})

    def listar_marca(request):
        productos = Producto.objects.all()
        return render(request, "ListaMarca.html", {"productos": productos})

    def listar_categoria(request):
        productos = Producto.objects.all()
        return render(request, "ListaCategoria.html", {"productos": productos})

    def edit(request, id_producto):
        producto = Producto.objects.filter(id=id_producto).first()
        form = FormularioProducto(instance=producto)
        return render(request, "ProductoEdit.html", {"form": form, "producto": producto})

    def actualizar_producto(request, id_producto):
        producto = Producto.objects.get(pk=id_producto)
        form = FormularioProducto(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        productos = Producto.objects.all()
        return render(request, "ListaCategoria.html", {"productos": productos})

    def delete(request, id_producto):
        producto = Producto.objects.get(pk=id_producto)
        producto.delete()
        productos = Producto.objects.all()
        return render(request, "ListaCategoria.html", {"productos": productos, "mensaje": "ok"})

class FormularioCategoriaView(HttpRequest):

    def index(request):
        categoria = FormularioCategoria()
        return render(request, "CategoriaIndex.html", {"form": categoria})

    def procesar_formulario(request):
        categoria = FormularioCategoria(request.POST)
        if categoria.is_valid():
            categoria.save()
            categoria = FormularioCategoria()
        return render(request, "CategoriaIndex.html", {"form": categoria, "mensaje": "ok"})

    def listar_productos(request):
        productos = Producto.objects.all()
        return render(request, "ListaProducto.html", {"productos": productos})

    def listar_marca(request):
        productos = Producto.objects.all()
        return render(request, "ListaMarca.html", {"productos": productos})

    def listar_categoria(request):
        productos = Producto.objects.all()
        return render(request, "ListaCategoria.html", {"productos": productos})

    def edit(request, id_producto):
        producto = Producto.objects.filter(id=id_producto).first()
        form = FormularioProducto(instance=producto)
        return render(request, "ProductoEdit.html", {"form": form, "producto": producto})

    def actualizar_producto(request, id_producto):
        producto = Producto.objects.get(pk=id_producto)
        form = FormularioProducto(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        productos = Producto.objects.all()
        return render(request, "ListaCategoria.html", {"productos": productos})

    def delete(request, id_producto):
        producto = Producto.objects.get(pk=id_producto)
        producto.delete()
        productos = Producto.objects.all()
        return render(request, "ListaCategoria.html", {"productos": productos, "mensaje": "ok"})



