from django.urls import path,include

from .views import book_list,book_detail,book_update,book_create

#  book/
urlpatterns = [
    path('', book_list , name='book_list'), 
    path('<int:pk>/', book_detail, name='book_detail'),
    path('<int:pk>/update/', book_update, name='book_update'),
    path('create/', book_create, name='book_create'),
]