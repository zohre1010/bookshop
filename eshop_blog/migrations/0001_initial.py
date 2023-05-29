# Generated by Django 4.1.2 on 2023-05-18 13:36

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='نام')),
                ('slug', models.SlugField(max_length=224, unique=True, verbose_name='نام در آدرس صفحه')),
                ('is_sub', models.BooleanField(default=False, verbose_name='آیا زیر مجموعه است')),
                ('available', models.BooleanField(default=True, verbose_name='فعال/غیرفعال')),
                ('sub_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scategory', to='eshop_blog.category', verbose_name='زیر مجموعه ی ')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='نام در آدرس صفحه')),
                ('image', models.ImageField(upload_to='', verbose_name='تصویر شاخص')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='توضیحات')),
                ('available', models.BooleanField(default=True, verbose_name='فعال/غیرفعال')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('writer', models.CharField(max_length=200, verbose_name='نویسنده')),
                ('category', models.ManyToManyField(related_name='blogs', to='eshop_blog.category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقاله ها',
                'ordering': ('name',),
            },
        ),
    ]
