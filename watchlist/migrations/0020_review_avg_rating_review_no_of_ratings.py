# Generated by Django 4.2.3 on 2023-08-17 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0019_review_author_alter_review_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='no_of_ratings',
            field=models.IntegerField(default=0),
        ),
    ]
