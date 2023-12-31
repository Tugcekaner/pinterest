# Generated by Django 4.2.1 on 2023-08-08 08:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pins', '0002_alter_image_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Pano Adı')),
                ('slug', models.SlugField(blank=True, verbose_name='Slug')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
            options={
                'verbose_name': 'Pano',
                'verbose_name_plural': 'Panolar',
            },
        ),
        migrations.CreateModel(
            name='Pintype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Kategori')),
                ('slug', models.SlugField(blank=True, verbose_name='Slug')),
            ],
        ),
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Pin adı')),
                ('text', models.TextField(verbose_name='İçerik')),
                ('image', models.FileField(upload_to='product', verbose_name='Pin Resmi')),
                ('date_now', models.DateField(auto_now_add=True, verbose_name='Tarih')),
                ('pano', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pins.pano', verbose_name='Pano')),
                ('pintype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pins.pintype', verbose_name='Kategori')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı - Satıcı')),
            ],
            options={
                'verbose_name': 'Pin',
                'verbose_name_plural': 'Pinler',
            },
        ),
    ]
