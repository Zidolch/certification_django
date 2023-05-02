from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from suppliers_network.views import NetworkObjectViewSet

router = routers.DefaultRouter()
router.register(r'network_objects', NetworkObjectViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
