# Generated by Django 4.1.2 on 2023-05-20 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_blog', '0002_alter_blog_writer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='created',
        ),
    ]
