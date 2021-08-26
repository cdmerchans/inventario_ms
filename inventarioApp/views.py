from django.shortcuts import render
from rest_framework.views import APIView
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from .models import Producto
from django.http import JsonResponse

class AgregarProducto(APIView):

    def post(self, request, *args, **kwargs):

        nombre = request.data['nombre'].capitalize()
        precio = request.data['precio']
        descripcion = request.data['descripcion']
        cantidad = request.data['cantidad']
        categoria = request.data['categoria']

        producto = Producto.objects.filter(nombre = nombre).values('id_producto')

        if not producto:

            new_product = Producto(nombre = nombre, precio = precio, descripcion =  descripcion, cantidad = cantidad, categoria = categoria)
            new_product.save()

            return Response({"mensaje": "Producto agregado"}, status=status.HTTP_201_CREATED)

        else:

            Producto.objects.filter(nombre = nombre).update(precio = precio, descripcion =  descripcion, cantidad = cantidad, categoria = categoria)
        
            return Response({"mensaje": "Producto actualizado"}, status=status.HTTP_200_OK)


    def delete(self, request):

        nombre = request.query_params.get('nombre', None)

        if nombre is None:

            return Response({"mensaje": "El nombre está vacio"},status=status.HTTP_404_NOT_FOUND)

        else:   
            
            nombre = nombre.capitalize()
            producto_base = Producto.objects.filter(nombre = nombre)

            if not producto_base:

                return Response({"mensaje": "El producto no existe"},status=status.HTTP_404_NOT_FOUND)

            else:

                producto_base.delete()

                return Response({"mensaje": "El producto fue eliminado"}, status=status.HTTP_200_OK)

    def get(self, request):

        nombre = request.query_params.get('nombre', None)
        
        if nombre is None:

            return Response({"mensaje": "El nombre está vacio"},status=status.HTTP_404_NOT_FOUND)

        else:

            nombre = nombre.capitalize()
            producto_base = Producto.objects.filter(nombre = nombre).values()
            
            if not producto_base:

                return Response({"mensaje": "El producto no existe"},status=status.HTTP_404_NOT_FOUND)

            else:

                producto_list = list(producto_base)

                return JsonResponse(producto_list, safe=False, status=status.HTTP_200_OK)

class VerProductos(APIView):

    def get(self, request, *args, **kwargs):

        productos = Producto.objects.all().values()
        productos_list = list(productos)

        return JsonResponse(productos_list, safe=False, status=status.HTTP_200_OK)

class BuscarProducto(APIView):

    def get(self, request, pk):

            producto_base = Producto.objects.filter(id_producto = pk).values()

            if not producto_base:

                return Response({"mensaje": "El producto no existe"},status=status.HTTP_404_NOT_FOUND)

            else:

                producto_list = list(producto_base)

                return JsonResponse(producto_list, safe=False, status=status.HTTP_200_OK)

class ActualizarCantidad(APIView):

    def put(self, request, *args, **kwargs):

        nombre = request.data['nombre'].capitalize()
        cantidad = request.data['cantidad']
        
        cantidad_base = Producto.objects.filter(nombre = nombre).values('cantidad')

        if not cantidad_base:

            return Response({"mensaje": "El producto no existe"},status=status.HTTP_404_NOT_FOUND)

        else:
            
            cantidad_base = cantidad_base[0]
            cantidad_base = int(cantidad_base["cantidad"])
             
            if -int(cantidad) > cantidad_base:

                return Response({"mensaje": "La cantidad es mayor a la disponible"}, status=status.HTTP_406_NOT_ACCEPTABLE)

            else:

                cantidad_nueva = int(cantidad_base)+int(cantidad)
                Producto.objects.filter(nombre = nombre).update(cantidad = cantidad_nueva)

                return Response({"mensaje": "Producto actualizado"}, status=status.HTTP_200_OK)
