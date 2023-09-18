# cd commerce_new/commerce 
# python manage.py runserver
# git commit -am ""
# git push origin main


from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User,Listings,Category,Comment,Bid
from django.core.exceptions import PermissionDenied


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
    listing_watchlst = listing.watchlist.filter(id=request.user.id).exists()
    comments = Comment.objects.filter(product=listing)
    bids = Bid.objects.filter(listing=id).order_by('-bid')
    largest_bid = Bid.objects.filter(listing=id).order_by('-bid').first()
    min_bid = largest_bid.bid 
    return render(request, "auctions/listing.html", {"listing": listing, "exists": listing_watchlst, "comments": comments, "bids": bids, "largest_bid": largest_bid, "min_bid": min_bid})
        #in listing make sure to filter through high to low, and atleast backed validation for bid is greater than highest bid

@login_required(login_url='auctions/login.html')
def watchlist(request):
    user = User.objects.get(id=request.user.id)
    listings = user.l_watchlist.all()
    return render(request, "auctions/index.html", {"listings":listings})
    
@login_required(login_url='auctions/login.html')
def addToWatchlist(request,id):
    user = request.user
    listing = Listings.objects.get(pk=id)
    listing.watchlist.add(user)
    return HttpResponseRedirect(reverse(watchlist))
    
@login_required(login_url='auctions/login.html')
def removeWatchlist(request, id):
     user = request.user
     listing = Listings.objects.get(pk=id)
     listing.watchlist.remove(user)
     return HttpResponseRedirect(reverse(watchlist))

def comment(request):
    if request.method == "POST":
        comment = request.POST['comment']
        Id = request.POST['id']
        product = Listings.objects.get(pk=Id)
        author = request.user
        C = Comment(author=author, product=product , comment=comment)
        C.save()
        return HttpResponseRedirect(reverse(listing, args=Id))


def make_bid(request):
    if request.method == "POST":
        if listing.active == False:
            raise PermissionDenied(" Sorry but bidding is closed !!!")
        bid = float(request.POST['bid'])        
        listing_id = request.POST['listing_id']
        largest_bid = Bid.objects.filter(listing=listing_id).order_by('-bid').first().bid
        if bid < largest_bid:
            raise PermissionDenied("Bid should be more than previous bids")
        owner = request.user
        
        listing = Listings.objects.get(pk=listing_id)
        new_bid = Bid(owner=owner, listing=listing, bid=bid)
        new_bid.save()
        return HttpResponseRedirect(reverse('listing', args=[listing.id]))

        #in listing make sure to filter through high to low, and atleast backed validation for bid is greater than highest bid


def close(request):
    if request.method == "POST":
        listing_id = request.POST["id"]
        listing = Listings.objects.get(pk=listing_id)
        listing.active = False
        listing.save()
        return HttpResponseRedirect(reverse("listing" , args=[listing_id]))
