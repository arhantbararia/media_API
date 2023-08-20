# Generated by Django 4.2.3 on 2023-08-13 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0006_rename_movieplatform_mediaplatform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='streamplatform',
            name='countries',
        ),
        migrations.AddField(
            model_name='media',
            name='country',
            field=models.ManyToManyField(related_name='media', to='watchlist.country'),
        ),
        migrations.DeleteModel(
            name='MediaPlatform',
        ),
    ]