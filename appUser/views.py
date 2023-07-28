from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
import random

def subscribeUser(request):
    context={}
    if request.method=="POST":
        submit=request.POST.get("submit")
        if submit=="subscribeButton":
            request.user.userinfo.subscribe=True
            request.user.userinfo.save()
            messages.warning(request, "Aboneliğiniz başarıyla oluşturuldu.")
            return redirect("profileUser")
        
    return render(request,'subscribe.html', context)


def profileUser(request):
    profile_list=Profile.objects.filter(user=request.user)
    
    if request.method=="POST":
        submit=request.POST.get("submit") 
        
        if submit == "profileLogin":
            pid=request.POST.get("id")
            profile=get_object_or_404(Profile, id=pid)
            
            #todo: Girişli olan profili bulmak
            profile_list.update(loginp=False) #todo:profillerin hepsinden çıkış yaptırıyor
            profile.loginp=True #todo: tıklanan profilin girişini yapıyor.
            profile.save()
            
            # todo: Girişli olan profili bulmak
            # for i in profile_list:
            #     i.loginp=False
            #     i.save()
                
            # profile.loginp=True
            # profile.save()
            
            return redirect("netflix")
           
        
        if submit == "profileCreate":
            # profil ekleme start
            if len(profile_list)<4:
                pname=request.POST.get("profileName")
                image=request.FILES.get("image")
            
                if pname.strip(" ") == "" or profile_list.filter(name=pname).exists(): #aynı isimli kullanıcı var mı diye baktık
                    messages.warning(request, "Profil Adını Gririniz ya da Değiştiriniz!!")
                    return redirect('profileUser')
                
            
                profile=Profile(name=pname, image=image, user=request.user) #request.user= girişli olan kullanıcıyı verir
            
                if image is None:
                    profile.image="profile/smile-icon.jpg"
            
                profile.save()
        
            else:
                messages.warning(request , "en fazla 4 profil oluşturabilirsiniz.")
        # profil ekleme end
        
        
        # profileDüzenleme start
        elif submit=="profileChange":
            
            pname2=request.POST.get("pname2")
            image2=request.FILES.get("image2")
            pid=request.POST.get("id")
            
            if pname2.strip(" ") == "" or profile_list.filter(name=pname2).exists(): #aynı isimli kullanıcı var mı diye baktık
                messages.warning(request, "Profil Adını Gririniz ya da Değiştiriniz!!")
                return redirect('profileUser')
            

            profile2 = profile_list.get(id=pid)
            profile2.name=pname2
            if image2 is not None:
                profile2.image=image2
            profile2.save()
            
            # profileDüzenleme end
            
            #formdan button ile Profile Silme start
        
        elif  submit == "profileDelete":
            pid=request.POST.get("id")
            profile=get_object_or_404(Profile, id=pid)
            profile.delete()
            
            #formdan button ile Profile Silme end
                  
        return redirect("profileUser")

    context={
        "profile_list":profile_list,
    }
    return render(request, 'browse.html', context)


#!URL ile profil silme start
# def deleteprofileUser(request,id):
#     #! filter yada 404 ü kullan
#     # profile=Profile.objects.filter(id=id).first() #todo: hatasız id çekme
#     profile=get_object_or_404(Profile, id=id) #todo: get ile aynıdır çekemediği durumda 404 sayfasına yönlendirir
#     profile.delete()
#     return redirect('profileUser')

#!URL ile profil silme start





def accountUser(request):
    profile=Profile.objects.filter(loginp=True, user=request.user).first()
    user=User.objects.filter(username=request.user).first()
    # user.check_password() #todo:password doğrulama
    
    if request.method=="POST":
        submit = request.POST.get("submit")
        
        if submit=="subscribeUnfollow":
            user.userinfo.subscribe= False
            user.userinfo.save()
            messages.warning(request,"aboneliğiniz İptal edilmiştir.")
            return redirect("accountUser")
        
        elif submit == "passwordUpdate":
            password= request.POST.get("password")
            passwordNew= request.POST.get("passwordNew")
            passwordAgain= request.POST.get("passwordAgain")

            if User.check_password(password) and (passwordNew==passwordAgain):
                user.userinfo.password=passwordNew
                user.userinfo.save()
                
                user.set_password(passwordNew) #todo: set_password: ilk passwordu değiştirir (içerisine de ne ile değiştirilsin). ayrıca çıkış yaptırdığı için takrardan giriş yapabilmesi için login sayfasına yönlendirilmeli
                user.save()
                return redirect("loginUser")
            else:
                messages.warning(request," şifre yanlış ya da şifreler aynı değil!!")
                
            
        
        elif submit == "telUpdate":
            tel=request.POST.get("tel")
            password=request.POST.get("password")
          
            if user.check_password(password):
                user.userinfo.tel=tel
                user.userinfo.save()
            else:
                messages.warning(request,"Şifre Yanlış !!")  
                

        elif submit == "emailUpdate":
            email=request.POST.get("email")
            password=request.POST.get("password")
            
            #!1. yöntem:
            email_bool=True
            if User.objects.filter(email=email).exists():
                email_bool=False
                messages.warning(request,"Girdiğiniz mail başkası tarafından kullanılıyor!!")            

            if user.check_password(password):
                if email_bool:
                    user.email=email
                    user.save()
            else:
                messages.warning(request,"Şifre Yanlış!!")
            
            
            #! 2. yöntem:
            # if user.check_password(password): #todo: kullanıcıdan aldığımız inputtan password doğru ile true yanlış ise false döndürecek
            #     if User.objects.filter(email=email).exists():    
            #         user.email =email
            #         user.save()
            #     else:
            #         messages.warning(request,"Bu email zaten kullanılıyor")
            # else:
            #     messages.warning(request,"Şifreniz yanlış!!")

        return redirect("accountUser")

            
    
    context={
        "profile":profile,
    }
    return render(request, 'hesap.html', context)


def loginUser(request):
    context= {}      
    if  request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        
        user=authenticate(username=username , password=password)
        
        if user is not None:
            login(request, user)
            
            if user.userinfo.subscribe:
                return redirect("profileUser")
            return redirect('subscribeUser')
        else:
            # context.update({"hata":"Kullanıcı adı veya şifre yanlış!"})
            messages.warning(request, "Kullanıcı adı veya şifre yanlış!")
            return redirect('loginUser')
        
        
            
            
            
        
    return render(request, 'login.html', context)
        
            

def registerUser(request):
    context={}
    
    if request.method=="POST":
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        username=request.POST.get("username")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")
        
        pasword_bool=email_bool=username_bool=True
        
        
        if password1 != password2:
            pasword_bool=False
            messages.warning(request, "şifreler aynı değil!")
        
        if User.objects.filter(email=email).exists():
            email_bool=False
            messages.warning(request, "E-Mail Daha önceden alınmıştır!")
        
        if User.objects.filter(username=username).exists():
            username_bool=False
            
            #todo: profil adı önerme
            infolist=[]
            i=0 
            while i<20:
                usernew = username 
                i +=1
                if len(infolist)>=3:
                    break
                
                lettercount = random.choice([1,2,3]) #todo:kaç haneli sayı üretecek önce 1 ,sonra2, en son 3 haneli
                for j in range(lettercount):
                    letterrandom=random.randint(0,9) 
                    usernew += str(letterrandom)
                    
                if (usernew  not in infolist) and (not User.objects.filter(username=usernew).exists()):
                    infolist.append(username)
                    messages.info(request, usernew)
            
            
            
            
            messages.warning(request, "Sisteme kayıtlı böyle bir kullanıcı vardır!")
           
        if pasword_bool and email_bool and username_bool:
            user=User.objects.create_user(first_name=fname, last_name=lname, email=email, username=username, password=password1)
            user.save()
            
            userinfo=Userinfo(user=user, password=password1)
            userinfo.save()
        
            return redirect("loginUser")
    

    return render(request, 'register.html', context)

def logoutUser(request):
    logout(request)
    return redirect("indexPage")


