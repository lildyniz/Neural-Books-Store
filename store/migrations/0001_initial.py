# Generated by Django 4.2.10 on 2024-02-19 21:10

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
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('birth', models.DateField()),
                ('image', models.ImageField(blank=True, upload_to='authors/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'author',
                'verbose_name_plural': 'authors',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['name'],
                'indexes': [models.Index(fields=['name'], name='store_categ_name_1278fd_idx')],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='books/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available', models.BooleanField(default=True)),
                ('written', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ManyToManyField(related_name='author_books', to='store.author')),
                ('category', models.ManyToManyField(related_name='books', to='store.category')),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
                'ordering': ['name'],
            },
        ),
        migrations.AddIndex(
            model_name='author',
            index=models.Index(fields=['name'], name='store_autho_name_28e2a0_idx'),
        ),
        migrations.AddIndex(
            model_name='author',
            index=models.Index(fields=['birth'], name='store_autho_birth_d8f1f6_idx'),
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['id', 'slug'], name='store_book_id_8b3379_idx'),
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['name'], name='store_book_name_b1097f_idx'),
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['-created'], name='store_book_created_2206b2_idx'),
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['-written'], name='store_book_written_bc508c_idx'),
        ),
    ]
