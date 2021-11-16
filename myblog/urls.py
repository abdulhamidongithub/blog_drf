from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app1.views import MaqolaViewSet, RasmViewSet

router = DefaultRouter()
router.register('maqola',MaqolaViewSet)
router.register('rasm',RasmViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
