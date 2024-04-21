from rest_framework import viewsets,mixins

from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookMixinViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        # email = serializer.validated_data.pop('email')
        # print(email) 
        title = serializer.validated_data['title']
        description = serializer.validated_data.get('description') or None
        author = serializer.validated_data.get('author') or None
        
        if description is None or author is None:
            description = title
            author = 'Unknown'
        serializer.save(description=description)
    
        return super().perform_create(serializer)


book_list = BookMixinViewSet.as_view({'get':'list'})
book_detail = BookMixinViewSet.as_view({'get':'retrieve'})
book_update = BookMixinViewSet.as_view({'put':'update'})
book_create = BookMixinViewSet.as_view({'post':'create'})


# to get the request in viewset or genaric view :
#       request = self.request 
# to get the request in serializer :
#       request = self.context.get('request')