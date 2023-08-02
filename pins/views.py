from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def indexPage(request):
     images = Image.objects.all()

     context={
          'images': images
     }

     return render(request,'index.html',context)



