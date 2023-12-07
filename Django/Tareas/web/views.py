from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.urls import reverse, reverse_lazy

from web.models import producto


#Acá se muestran las vistas de todo lo que va a ver el usuario en la pagina

def index(request):
    return render(request, 'web/index.html') #Junta la plantilla y la informacion consiguiendo renderizarlo en un html (Lo que el usuario termina viendo)


class ProductoListView(ListView):
    model = producto
    context_object_name = 'lista_producto'
    template_name = 'web/lista_de_productos.html'


class ProductoCreateView(CreateView):
    model = producto
    template_name = 'web/crear_productos.html'
    success_url = 'lista'
    fields = '__all__' # Se lo puede reeemplazar por: ['nombre_producto', 'descripcion']


class ProductoDetailView(DetailView):
    model = producto
    template_name = 'web/producto_detalle.html'



class ProductoUpdateView(UpdateView):
    model = producto
    template_name = 'web/modificar_producto.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('modificar_producto', kwargs={'pk': self.object.pk})
    
class ProductoDeleteView(DeleteView):
    model = producto
    template_name = 'web/borrar_producto.html'
    success_url = reverse_lazy('lista_producto')