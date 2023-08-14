from django.db import models
from user.models import *
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    

class Pintype(models.Model):
    title = models.CharField(("Kategori"), max_length=50)
    slug = models.SlugField(("Slug"), blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Pano(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    title = models.CharField(("Pano Adı"), max_length=50)
    slug = models.SlugField(("Slug"), blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Panolar'
        verbose_name = 'Pano'


    def __str__(self):
        return self.title

    
class Pin(models.Model):
    user = models.ForeignKey(User, verbose_name=(
        "Kullanıcı"), on_delete=models.CASCADE)
    pintype = models.ForeignKey(Pintype, verbose_name=(
        "Kategori"), on_delete=models.CASCADE,null=True, default='pin')
    pano = models.ForeignKey(Pano, verbose_name=(
        "Pano"), on_delete=models.CASCADE,null=True)
    title = models.CharField(("Pin adı"), max_length=50)
    text = models.TextField(("İçerik"))
    image = models.FileField(
        ("Pin Resmi"), upload_to='pin', max_length=100)
    date_now = models.DateField(("Tarih"), auto_now_add=True)

    def __str__(self):  
        return self.title
    
    class Meta:
        verbose_name_plural = 'Pinler'
        verbose_name = 'Pin'


