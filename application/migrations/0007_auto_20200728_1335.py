# Generated by Django 3.0.8 on 2020-07-28 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_posts_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=models.TextField(max_length=350),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.TextField(max_length=255),
        ),
    ]
