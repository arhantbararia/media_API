# Generated by Django 4.2.3 on 2023-08-13 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0014_remove_media_language'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Language',
        ),
    ]
