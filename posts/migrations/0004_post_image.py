# Generated by Django 3.2.8 on 2021-10-18 02:57

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, db_index=True, max_length=255, verbose_name='image'),
        ),
    ]
