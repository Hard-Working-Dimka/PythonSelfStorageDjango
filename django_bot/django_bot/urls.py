from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from self_storage.views import ClientsApiView

router = routers.DefaultRouter()
router.register(r'api/clients', ClientsApiView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
