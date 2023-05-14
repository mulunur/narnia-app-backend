from itemsImages.api.views import ItemsViewSet
from itemsImages.api.views import APIView
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()

router.register(r'items', ItemsViewSet)

urlpatterns = [
    path('', include(router.urls))
]