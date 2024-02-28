from rest_framework import viewsets,mixins

from .models import Book
from .serializers import BookSerilizer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerilizer

class BookMixinViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerilizer