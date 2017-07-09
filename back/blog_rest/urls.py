from django.conf.urls import url, include
from rest_framework import routers
from blog_rest.viewsets import PostViewSet, CityViewSet, RegionViewSet, ImageViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet, 'posts')
router.register('cities', CityViewSet, 'cities')
router.register('regions', RegionViewSet, 'regions')
router.register('upload_images', ImageViewSet, 'upload_images')


# urlpatterns = [
#     url(r'^', include(router.urls))
# ]
urlpatterns = router.urls