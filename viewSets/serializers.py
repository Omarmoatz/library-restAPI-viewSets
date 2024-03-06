from rest_framework import serializers 

from .models import Book

class BookSerilizer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    url = serializers.HyperlinkedIdentityField(
        view_name= 'book_detail',
        lookup_field= 'pk'
    )
    class Meta:
        model = Book
        fields = '__all__'