from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'Authors'
        db_table = 'authors'


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=200)

    def __str__(self):
        return self.publisher_name

    class Meta:
        verbose_name_plural = 'Publishers'
        db_table = 'publishers'


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories'
        db_table = 'categories'


class Book(models.Model):
    book_name = models.CharField(max_length=100)
    book_image = models.ImageField(upload_to='images/books', default='images/books/book.jpg')
    book_descriptions = models.TextField()
    book_author = models.ManyToManyField(Author),
    book_publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE),
    book_category = models.ManyToManyField(Category)
    book_pages = models.ImageField()
    book_file = models.FileField(upload_to='books')
    book_year = models.IntegerField()

    def __str__(self):
        return self.book_name

    class Meta:
        verbose_name_plural = 'Books'
        db_table = 'books'
        ordering = ['-id']
