from django.shortcuts import render,redirect

# Create your views here.
def indexPage(request):
     return render(request,'index.html')
