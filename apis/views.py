from rest_framework import generics
from books.models import Book
from .serializers import BookSerializers

# Create your views here.

class BookApiView(generics.ListAPIView):
    #queryset es un parametro que define la consulta a realizar en la base de datos# 
    queryset = Book.objects.all()
    serializer_class = BookSerializers