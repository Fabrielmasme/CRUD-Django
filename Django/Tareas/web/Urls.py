from django.urls import path
from . import views

#Acá se definen las urls que se van a estar utiluzando en las diferentes paginas de la app

urlpatterns = [
    #path('listado' , views.lista_producto, name="crear_producto")

    #camino('Nombre de la pagina', vista.Accion de lo que hace la pagina, nombre="(Es el nombre que sirve en el archivo views)")

    path('', views.index, name='index'),  #Acá lo que se hace es poner las urls que va a haber dentro de la app con el path(Camino)
    path('crear' , views.ProductoCreateView.as_view(), name="crear_producto"),

    path('lista', views.ProductoListView.as_view(), name="lista_producto"),

    path('detalle/<pk>', views.ProductoDetailView.as_view(), name='producto_detalle'),

    path("modificar/<pk>/", views.ProductoUpdateView.as_view(), name="modificar_producto"),

    path("borrar/<pk>/", views.ProductoDeleteView.as_view(), name="borrar_producto"),
]