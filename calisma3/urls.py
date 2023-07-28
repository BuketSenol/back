
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from appMy.views import *
from appUser.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',indexPage, name='indexPage'),
    path('netflix',netflix, name='netflix'),  #todo: url de profil id si belli değil
    path('netflix/test', listem, name="listem"),
    path('netflix/<catetitle>', movieType, name="movieType"),
   
    # path('netflixPage<id>',netflixPage, name='netflixPage'),  #todo: url de profil id si belli 
    
    #====USER====#
    path("subscribeUser", subscribeUser, name="subscribeUser"),
    path('profileUser',profileUser, name='profileUser'),
    # path('deleteprofileUser<id>',deleteprofileUser, name='deleteprofileUser'),  #todo: url de profile silme
    path('accountUser',accountUser, name='accountUser'),
    path('loginUser',loginUser, name='loginUser'),
    path('registerUser',registerUser, name='registerUser'),
    path('logoutUser',logoutUser, name='logoutUser'),
    
    
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
