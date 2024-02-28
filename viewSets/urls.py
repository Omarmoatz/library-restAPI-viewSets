from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import BookViewSet,BookMixinViewSet

router = DefaultRouter()
router.register('viewSets', BookViewSet)
router.register('viewSets/mixins', BookMixinViewSet,basename='book-mixins')

urlpatterns = [
    path('', include(router.urls)),
]