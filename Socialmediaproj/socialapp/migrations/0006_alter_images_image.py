# Generated by Django 4.1.1 on 2022-11-19 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0005_alter_article_likes_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
