#commerce_new/commerce
#python manage.py runserver


from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User,Listings,Category


def index(request):
    listings = Listings.objects.all()
    return render(request, "auctions/index.html", {"listings":listings})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required(login_url='auctions/login.html')
def new(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, "auctions/new.html" , {"categories":categories})
    else:
        #user posted to this route
        name = request.POST["title"]
        description = request.POST["description"]
        image_url = request.POST["image_url"]
        price = request.POST["price"]
        category = request.POST["category"]
        category_of_listing = Category.objects.get(name=category)
        user = request.user
        if not image_url:
            listing = Listings( owner=user ,title=name , description=description ,price=price, category=category_of_listing)
        else:
            listing = Listings( owner=user  ,title=name , description=description ,imageUrl=image_url , price=price, category=category_of_listing)
        listing.save()
        return HttpResponseRedirect(reverse("index"))         


def category(request):
    categories = Category.objects.all()
    return render(request, "auctions/category.html" , {"categories":categories})

def category_similar(request, name):
        cateory = Category.objects.get(name=name)
        listings = Listings.objects.filter(category=cateory)
        return render(request, "auctions/category_similar.html" , {"listings":listings})


def listing(request, id):
    listing = Listings.objects.get(id=id)
    return render(request, "auctions/listing.html" , {"listing":listing})


def watchlist(request):
    user = User.objects.get(id=request.user.id)
    listings = user.l_watchlist.all()
    return render(request, "auctions/index.html", {"listings":listings})