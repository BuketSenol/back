from django.db import models

class Category(models.Model):
    catetitle=models.CharField(("Kategori"), max_length=50)
    
    def __str__(self):
        return self.catetitle
    
class Type(models.Model):
    type= models.CharField(("Tür"), max_length=50)
    
    def __str__(self):
        return self.type
    
class Card(models.Model):
    category=models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE)
    type=models.ForeignKey("Type", verbose_name=("Tür"), on_delete=models.CASCADE, null=True)
    title=models.CharField(("Film/dizi"), max_length=50)
    image=models.ImageField(("Resim"), upload_to="image", max_length=200)
    listLike=models.BooleanField(("Listem"), default=False, null=True)
    
    def __str__(self):
        return self.title
