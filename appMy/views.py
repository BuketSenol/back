from django.shortcuts import render,get_object_or_404, redirect
from appUser.models import Profile
from .models import*
from django.contrib.auth.models import User
from appUser.models import Userinfo



def indexPage(request):
    context={}
    return render(request, 'index.html', context)


# def netflixPage(request , id):  #todo: url de profilin id'sinin gözükmesi 
#     profile=get_object_or_404(Profile, id=id)
#     context={
#         "profile":profile,
#     }
#     return render(request, 'browse-index.html', context)


def netflix(request):
    profile=Profile.objects.filter(loginp=True, user=request.user).first()
    category=Category.objects.all()
    movieCard = Card.objects.all()
    
    if request.method=="POST":
        cardId=request.POST.get("listLike")
        print("caard:", cardId)
        movieCard = Card.objects.filter(id=int(cardId)).first()
        if movieCard:
            movieCard.listLike =True
            movieCard.save()
        
        return redirect("movieType", movieCard.category.catetitle)
        
    
    context={
        "profile":profile,
        'category':category,
        'movieCard':movieCard
    }
    return render(request, 'browse-index.html', context)


def listem(request):
    context = {}
    category = Category.objects.all()
    context['category'] = category
    profile=Profile.objects.filter(loginp=True, user=request.user).first()
    context['profile'] = profile  
    card = Card.objects.filter(listLike=True)
    context["cards"] = card
    if request.method=="POST":
        cardId=request.POST.get("unLike")
        print("caard:", cardId)
        movieCard = Card.objects.filter(id=int(cardId)).first()
        if movieCard:
            movieCard.listLike =False
            movieCard.save()
        
    return render(request, 'listem.html', context)


    # types of movies(action, comedy etc.)
def movieType(request, catetitle=None):
    profile = Profile.objects.filter(loginp=True, user=request.user).first()
    category = Category.objects.all()
    type = Type.objects.all()
    ogeler = {}
    card = None

    for tip in type:
        movies = Card.objects.filter(type=tip,category__catetitle=catetitle)
        if movies.__len__():
            for movie in movies:
                ogeler[tip.type] = movies
                
    if catetitle is None:
        card = Card.objects.all()
    else:
        # filmler/diziler opsiyon vs
        card = Card.objects.filter(category__catetitle=catetitle, listLike=True)

    context = {
        "profile": profile,
        "category": category,
        "type_data": type,
        "card": card,
        "catetype" : ogeler.items(),
    }

    return render(request, 'movie-type.html', context)
    
    

  
        
    
    

    