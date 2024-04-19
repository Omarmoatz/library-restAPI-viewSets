from rest_framework import serializers 
from rest_framework.reverse import reverse

from .models import Book

class BookSerilizer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    edite_url = serializers.SerializerMethodField(method_name='get_url')
    url = serializers.HyperlinkedIdentityField(
        view_name= 'book_detail',
        lookup_field= 'pk'
    )
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Book
        fields = '__all__'


    def create(self, validated_data):
        # email = validated_data.pop('email')
        item = super().create(validated_data)
        # send email to someone
        return item

    def get_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('book_update' ,kwargs={'pk':obj.pk} ,request=request)