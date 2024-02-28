from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=200, default='defaut_title')
    author = models.ForeignKey('Author' ,related_name='book_author', on_delete=models.SET_NULL, null=True, blank=True)
    publication_date = models.DateField(default=timezone.now)
    description = models.TextField(max_length=1000,  default='defaut_description')
    price = models.DecimalField( max_digits=6, decimal_places=2, default=99.99)

    
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title


GENDER_CHOICES = (
    ('Male','Male'),
    ('Female','Female'),
)
class Author(models.Model):
    name = models.CharField(max_length=200, default='author1')
    age = models.PositiveIntegerField(default=99)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    birth_date = models.DateField(default=timezone.now)
    biography = models.TextField(max_length=1000, default='defaut_biography')

    
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name
