from rest_framework import serializers 
from rest_framework.reverse import reverse

from .models import Book
from . import validators

class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    edite_url = serializers.SerializerMethodField(method_name='get_url')
    url = serializers.HyperlinkedIdentityField(
        view_name= 'book_detail',
        lookup_field= 'pk'
    )
    email = serializers.EmailField(write_only=True)
    title = serializers.CharField(validators=[validators.unique_title, validators.validate_no_test])
    name = serializers.CharField( source='title', read_only=True) 

    class Meta:
        model = Book
        fields = '__all__'

    # def validate_field name()

    # def validate_title(self,value):             # I should use the validator in the serializer 
    #     request = self.context.get('request')   #   if i wanted to use the request like this example 
    #     user = request.user                                
    #     qs = Book.objects.filter( user=user ,title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f'{value} this book is already exists')
    #     return value


    def create(self, validated_data):
        email = validated_data.pop('email')         # you should do any edite in the serializer
                                                    #   rather than in the view if you can
        item = super().create(validated_data)
        # send email to someone
        return item
    
    def update(self, instance, validated_data):
        email = validated_data.pop('email') 
        description = validated_data.get('description') or None

        if description is None:
            instance.description = 'test update method in serializer'

        return super().update(instance, validated_data)

    def get_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('book_update' ,kwargs={'pk':obj.pk} ,request=request)