from django.urls import path
from rest_framework.routers import DefaultRouter

from app_library.views import AuthorViewSet, PublisherViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'publisher', PublisherViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = router.urls
