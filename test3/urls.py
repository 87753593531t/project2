from rest_framework.routers import DefaultRouter
from rest_framework.urls import path

from test3.views import LaptopViewSet

router = DefaultRouter()


router.register('laptop', LaptopViewSet)


urlpatterns = [
    # path('laptops/', LaptopViewSet.as_view({'get': 'list'})),
]+router.urls