from rest_framework import viewsets,mixins

from .models import Book
from .serializers import BookSerilizer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerilizer

class BookMixinViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerilizer


book_list = BookMixinViewSet.as_view({'get':'list'})
book_detail = BookMixinViewSet.as_view({'get':'retrieve'})
book_update = BookMixinViewSet.as_view({'put':'update'})