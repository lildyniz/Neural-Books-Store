# Generated by Django 4.2.10 on 2024-02-20 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='autor',
            new_name='author',
        ),
    ]