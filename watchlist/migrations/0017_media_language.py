# Generated by Django 4.2.3 on 2023-08-13 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0016_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='language',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='watchlist.language'),
        ),
    ]
