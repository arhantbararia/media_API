# Generated by Django 4.2.3 on 2023-08-17 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0021_remove_review_avg_rating_remove_review_no_of_ratings_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='no_of_ratings',
            field=models.IntegerField(default=0),
        ),
    ]
