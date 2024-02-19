# Generated by Django 5.0.2 on 2024-02-19 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('birth', models.DateField()),
                ('image', models.ImageField(blank=True, upload_to='autors/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'autor',
                'verbose_name_plural': 'autors',
                'ordering': ['name'],
                'indexes': [models.Index(fields=['name'], name='shop_autor_name_2cb8a2_idx'), models.Index(fields=['birth'], name='shop_autor_birth_d7c9a6_idx')],
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
                'indexes': [models.Index(fields=['name'], name='shop_catego_name_289c7e_idx')],
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
                ('autor', models.ManyToManyField(related_name='autors', to='shop.autor')),
                ('category', models.ManyToManyField(related_name='books', to='shop.category')),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
                'ordering': ['name'],
                'indexes': [models.Index(fields=['id', 'slug'], name='shop_book_id_1d2d16_idx'), models.Index(fields=['name'], name='shop_book_name_e113ac_idx'), models.Index(fields=['-created'], name='shop_book_created_5a3664_idx'), models.Index(fields=['-written'], name='shop_book_written_5a845a_idx')],
            },
        ),
    ]
