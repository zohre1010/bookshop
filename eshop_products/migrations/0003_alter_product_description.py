# Generated by Django 4.1.2 on 2023-05-20 06:28

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0002_product_visit_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]