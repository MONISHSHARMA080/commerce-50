# commerce-50

## Description
Commerce is an eBay-like e-commerce auction site that allows users to post auction listings, place bids on listings, comment on those listings, and add listings to a "watchlist." This project is part of the CS50W course, and it's designed to help you learn web development with Django.


Commerce - eBay-like E-commerce Auction Site
Commerce Logo <!-- Replace with your logo if desired -->

Table of Contents
Description
Getting Started
Understanding
Specification
Contributing
License
Description
Commerce is an eBay-like e-commerce auction site that allows users to post auction listings, place bids on listings, comment on those listings, and add listings to a "watchlist." This project is part of the CS50W course, and it's designed to help you learn web development with Django.

Note: If you are attempting this project without having watched Lecture 4, you're trying this too soon! Make sure you have the necessary background knowledge before proceeding.

Features
Active Listings Page: Display all currently active auction listings, including title, description, current price, and photos (if available).

Listing Page: View detailed information about a specific listing, including the current price. Users can add the item to their watchlist, bid on the item, or close the auction if they are the creator.

Create Listing: Users can create new listings, providing a title, description, starting bid, optional image URL, and category.

Watchlist: Users can add and remove listings from their watchlist. They can view all the listings they have added to their watchlist.

Categories: Users can browse listings by category, viewing all active listings within a specific category.

Comments: Users can add comments to listing pages, and all comments are displayed on the listing page.

Django Admin Interface: Site administrators can manage listings, comments, and bids through the Django admin interface.

Getting Started
Download the distribution code from here and unzip it.

Open your terminal and navigate to the commerce directory.

Run the following commands to set up your database:

Copy code
python manage.py makemigrations auctions
python manage.py migrate
Start the Django web server:

Copy code
python manage.py runserver
Visit the website in your browser. You can now register for an account and explore the features of the application.

### Understanding
In this section, you'll find an overview of the project structure and key components.

## URLs: URL configuration is defined in auctions/urls.py, including routes for login, logout, register, and more.

## Views: Views associated with each route are defined in auctions/views.py. These views handle user registration, login, logout, and index rendering.

## Templates: The HTML layout of the application is defined in auctions/templates/auctions/layout.html. It includes conditional rendering based on user authentication status.

## Models: auctions/models.py is where you define models for your application, including User, auction listings, bids, comments, and categories. Remember to run makemigrations and migrate when you make changes to models.

## Specification
To complete the implementation of your auction site, ensure that you fulfill the following requirements:

## Models: 
Create at least three models (in addition to the User model) for auction listings, bids, and comments. Customize the fields as needed.

## Create Listing:
Implement a page where users can create new listings with a title, description, starting bid, optional image URL, and category.

## Active Listings Page: 
The default route should display all active listings, including title, description, current price, and photos (if available).

## Listing Page:
Users can view detailed information about a specific listing, including the current price. Signed-in users can add the item to their watchlist, bid on the item, or close the auction (if they are the creator). The page should indicate if a user has won the auction.

## Watchlist:
Implement a page where signed-in users can view their watchlist and add/remove listings from it.

## Categories: 
Users can browse listings by category, viewing all active listings within a specific category.

## Comments:
Allow signed-in users to add comments to listing pages, displaying all comments on the listing page.

## Django Admin Interface:
Site administrators can manage listings, comments, and bids through the Django admin interface.(available on {root}/admin)

### Contributing
You are  welcome to  contribute and  improve Commerce. Feel free to open issues or pull requests for enhancements or bug fixes.
.I was going to Integrate react in this and if you want to go head  feel free

### [course/project's website](https://cs50.harvard.edu/web/2020/projects/2/commerce/)


