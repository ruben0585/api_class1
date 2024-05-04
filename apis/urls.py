from django.urls import path
from .views import BookApiView

urlpatterns = [
    path('', BookApiView.as_view(), name='book_list'),
]

#path es una funcion que permite crear rutas
#as_view() es una funcion que permite crear vistas basadas en clases
#name es un nombre que le damos a la ruta
#urlpattern es una lista de rutas que se encuentran en el proyecto 
#book_list es el nombre de la ruta que se crea en este archivo
#urls.py es el archivo que contiene las rutas del proyecto