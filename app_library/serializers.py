from rest_framework import serializers
from app_library.models import Author, Category, Publisher, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'book_name', 'book_image', 'book_year', 'book_author', 'book_file']


class BookAllInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
