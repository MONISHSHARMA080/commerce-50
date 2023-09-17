from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=64, blank=False)

    def __str__(self):
        return f"{self.name}"
    


class Listings(models.Model):
    title = models.CharField(max_length=64)
    description =  models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='user')
    imageUrl = models.URLField(blank=True , null=True)
    date_created = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,  blank=False)
    price = models.FloatField(max_length=10, blank=False)
    watchlist = models.ManyToManyField(User,blank=True ,null=True, related_name="l_watchlist")


    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) 
    comment = models.CharField(max_length=400)
    product = models.ForeignKey(Listings, on_delete=models.CASCADE, blank=True, null=True)    

    def __str__(self):
        return f"{self.author} on {self.product}"