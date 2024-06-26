# Generated by Django 5.0.4 on 2024-04-19 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Authors',
                'db_table': 'authors',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Publishers',
                'db_table': 'publishers',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('book_image', models.ImageField(default='images/books/book.jpg', upload_to='images/books')),
                ('book_descriptions', models.TextField()),
                ('book_pages', models.ImageField(upload_to='')),
                ('book_file', models.FileField(upload_to='books')),
                ('book_category', models.ManyToManyField(to='app_library.category')),
            ],
            options={
                'verbose_name_plural': 'Books',
                'db_table': 'books',
                'ordering': ['-id'],
            },
        ),
    ]
