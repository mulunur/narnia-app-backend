from rest_framework import routers
from .views import ItemsViewSet
from  django.urls import path, include
from rest_framework.views import APIView

router = routers.DefaultRouter()

#/api/items
router.register(r'items', ItemsViewSet)
#router.register(r'items', APIView)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:id>', include(router.urls)),
]

