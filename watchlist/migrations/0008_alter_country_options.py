# Generated by Django 4.2.3 on 2023-08-13 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0007_remove_streamplatform_countries_media_country_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Country', 'verbose_name_plural': 'Countries'},
        ),
    ]
