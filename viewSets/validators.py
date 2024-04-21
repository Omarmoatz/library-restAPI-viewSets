from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Book

# def validate_title(value):
#     qs = Book.objects.filter(title__iexact=value)
#     if qs.exists():
#         raise serializers.ValidationError(f'{value} this book is already exists')
#     return value

def validate_no_test(value):
    if 'test' == value.lower():
        raise serializers.ValidationError('the title must not contain test word ')
    return

unique_title = UniqueValidator(queryset=Book.objects.all())