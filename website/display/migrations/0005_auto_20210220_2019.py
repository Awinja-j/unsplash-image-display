# Generated by Django 3.1.7 on 2021-02-20 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0004_auto_20210220_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unsplash_photos',
            name='ai_primary_landmark_latitude',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='unsplash_photos',
            name='ai_primary_landmark_longitude',
            field=models.FloatField(default=None, null=True),
        ),
    ]
