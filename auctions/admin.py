from django.contrib import admin
from .models import Category,User,Listings

# Register your models here.
admin.site.register(Listings)
admin.site.register(User)
admin.site.register(Category)