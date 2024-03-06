from django.urls import path,include

from .views import book_list,book_detail

#  book/
urlpatterns = [
    path('list/', book_list , name='book_list'), 
    path('list/<int:pk>/', book_detail, name='book_detail'),
]