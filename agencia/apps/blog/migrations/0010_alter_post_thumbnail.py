# Generated by Django 3.2.16 on 2022-11-12 11:14

import apps.blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(max_length=500, upload_to=apps.blog.models.blog_thumbnail_directory),
        ),
    ]