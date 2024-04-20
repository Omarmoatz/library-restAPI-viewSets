from rest_framework import serializers

from .models import Book

def validate_title(value):
    qs = Book.objects.filter(title__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(f'{value} this book is already exists')
    return value