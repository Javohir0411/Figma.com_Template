from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from app_library.models import Author, Publisher, Category, Book
from app_library.permissions import MyPermissions
from app_library.serializers import (
    AuthorSerializer,
    PublisherSerializer,
    CategorySerializer,
    BookAllInfoSerializer,
    BookListSerializer,
)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [MyPermissions]


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [MyPermissions]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [MyPermissions]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    # serializer_class = BookSerializer
    permission_classes = [MyPermissions]

    def get_serializer_class(self):
        if self.action == 'list':
            return BookListSerializer
        else:
            return BookSerializer
