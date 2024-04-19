from rest_framework.routers import DefaultRouter

from .views import BookViewSet,BookMixinViewSet


#  book/
router = DefaultRouter()
router.register('viewSets', BookViewSet)

urlpatterns = router.urls