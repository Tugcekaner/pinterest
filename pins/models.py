from django.db import models
from user.models import *


# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title