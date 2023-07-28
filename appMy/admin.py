from django.contrib import admin

from .models import*

admin.site.register(Category)
admin.site.register(Type)

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    

    list_display = (  'category', 'id','title' , 'type')