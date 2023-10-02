# commerce-50

## Description
Commerce is an eBay-like e-commerce auction site that allows users to post auction listings, place bids on listings, comment on those listings, and add listings to a "watchlist."


Commerce - eBay-like E-commerce Auction Site

Getting Started
Download the distribution code from here and unzip it.

Open your terminal and navigate to the commerce directory.

Run the following commands to set up your database:

Copy code
python manage.py makemigrations auctions
python manage.py migrate
Start the Django web server: python manage.py runserver
Visit the website in your browser(local host). You can now register for an account and explore the features of the application.


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


