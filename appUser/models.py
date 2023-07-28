from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.ForeignKey(User, verbose_name=("Kullanıcı Adı"), on_delete=models.CASCADE, null=True)
    name=models.CharField(("Profil Adı"), max_length=50)
    image=models.ImageField(("Profil Resmi"), upload_to="Profile",  max_length=200)
    loginp=models.BooleanField(("Girişşli Profile"), default=False)

    def __str__(self):
        return self.user.username
    
class Userinfo(models.Model):
    user = models.OneToOneField(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    password = models.CharField(("Kullanıcı Şifresi"), max_length=50)
    tel = models.CharField(("Telefon"), max_length=50, default="-")
    subscribe=models.BooleanField(("Abonelik"), default=False)
    
    
    def __str__(self):
        return self.user.username
    

    