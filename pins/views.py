from django.shortcuts import render, redirect
from .models import *
from user.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
import time


# Create your views here.

# ! Ana sayfa
def indexPage(request):
     images = Image.objects.all()

     context={
          'images': images
     }

     if request.method == 'POST':
          if 'login_submit' in request.POST:

               username = request.POST.get('username')
               # email = request.POST.get('email')
               password = request.POST.get('password')

               user = authenticate(request, username=username, password=password)

               if user is not None:
                    login(request, user)
                    context['profile'] = user
                    messages.success(request, 'Hoşgeldin '+ user.username + '!')
                    return redirect("index")
               else:
                    messages.warning(request, 'Kullanıcı Adı veya şifre yanlış!!')
                    time.sleep(2)
                    return redirect("index")

          elif 'register_submit' in request.POST:
               username = request.POST.get("username")
               email = request.POST.get("email")
               password1 = request.POST.get("password1")
               password2 = request.POST.get("password2")
               print("-------------------------------------------------------------------------------")
               print(request.POST)


               if password1 == password2:
                    if not User.objects.filter(username=username).exists():
                         if not User.objects.filter(email=email).exists():
                              user = User.objects.create_user(
                                   username=username, email=email, password=password1)
                              userinfo = UserInfo(user=user)
                              userinfo.save()
                              messages.success(
                              request, 'Kaydınız başarıyla oluşturuldu..')
                              return redirect("index")
                         else:
                              messages.warning(request, 'Bu mail zaten kullanılıyor!!')
                              return redirect("index")
                    else:
                         messages.warning(
                         request, 'Bu kullanıcı adı daha önceden alınmış!!')
                         return redirect("index")
               else:
                    messages.warning(request, 'Şifreler aynı değil!!')
                    return redirect("index")

     return render(request,'index.html',context)



