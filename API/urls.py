from django.urls import path, include
from rest_framework import routers

from API.views import (
    CustomUserApiView, StorageApiView, StorageUnitApiView, OrderApiView
)

router = routers.DefaultRouter()
router.register(r'custom-user', CustomUserApiView)
router.register(r'storage', StorageApiView)
router.register(r'storage-unit', StorageUnitApiView)
router.register(r'order', OrderApiView)

urlpatterns = [
    path('', include(router.urls)),
]
