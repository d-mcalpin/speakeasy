# Speakeasy Cocktails
## Code Institute - Milestone 4 Project
### Live Heroku Link:

![Speakeasy Cocktails](demo link)

## Table of Contents
* [Summary](#summary)
* [Background](#background)
* [Aim of the Site](#aim-of-the-site)
* [Scope](#scope)
    * [User Stories](#user-stories)
* [Site Features](#site-features)
* [Future Features](#future-features)
* [Information Architecture](#information-architecture)
* [Skeleton](#skeleton)
    * [Mobile Wireframes](#mobile-wireframes)
    * [Tablet Wireframes](#tablet-wireframes)
    * [Desktop Wireframes](#desktop-wireframes)
    * [Changes to Wireframes](#changes-to-wireframes)
* [Structure](#structure)
* [Surface](#surface)
    * [Fonts](#fonts)
    * [Colours](#colours)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Meeting User Expectations](#meeting-user-expectations)
* [Deployment](#deployment)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

## Summary
Speakeasy Cocktails is an online coctail retailer, which specialises in delivering ready to drink cocktails and bar equipment direct to your home.

## Aim of the Site
Finding delicious cocktails can sometimes be tricky, particularly if you have to make them yourself.

The aim of the Speakeasy Cocktails website is to make this process finding great cocktails and enjoying them at home an easy and pleasant experience. On each product page, customers have the opportunity to read reviews about the cocktails and equipment that is for sale as well as the opportunit to add products to a wishlist in case they would like to try them in the future.

Products are displayed in an easy to use format where customers can search by keyword or find an item by category from anywhere on the site.

## Scope
Speakeasy Cocktail's primary target market is cocktail enthusiasts. We hope to encourage frequent purchases by offering customers an easy to use interface and a pleasant experience, while the ability to leave reviews may encourage customers to share knowledge and opinions with other customers. 

## Project Goals
### Target Audience
- People who are looking to buy cocktails and cocktail equipment
- People who unique and traditional cocktails
- People who want to try to make a cocktails at home by purchasing equipment by themselves
- People who want to read reviews about cocktails that have been left by other users

### Visitor / User Goals
- Purchase products in a smooth and secure way
- Get informed with the products before buying by reading product reviews / product information
- Inform other customers by leaving my own reviews
- Add products to my wishlist so that I can order them in the future

### Business Goals (Site Owner's Goals)
- Provide customers with a secure and safe ecommerce shop
- Establish the shop's brand image
- Expand their business effectively
- Make profit from selling products / services

<div><a href="#table-of-contents">Back to top</a></div>

## User Stories

- Viewing and Navigation

| AS A     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User/ Shopper | access the website with any devices | Use the website anytime and anywhere |
| Shopper | Easily see what services are offered | Find the service I want to use |  
| Shopper | All the important services are accesible from nav bar| I don't need to scroll or search to find important information |
| Shopper | Have a shopping cart icon on nav bar | Always check the current order and checkout when I want |

<br/>

- Registration, User Accounts and User Community

| AS A     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Easily register for an account | Have a personal account where I can edit my information |  
| Site User | View my order history | Purchase the same product again in the next order |
| Site User | Easily recover my password in case I forget it | Recover access to my account |
| Site User | Receive an email confirmation after registering | Verify that my account registration was successful |
| Site Owner | Let the site users log in when they leave comments/reviews | Track who left comments/reviews |

<br/>

- Online shopping

| AS A    | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Shopper | Search a product with keywords | Find the most appropriate products |
| Shopper | View individual product pages that have prices, descriptions, sizes, etc | Get detailed information about the product before purchasing |
| Shopper | Filter by a specific category | Easily find products in a specific category |
| Shopper | Add products to my wishlist to view later | Return to my sihlist to purchase products |
| Shopper/Site Owner | Leave/View product reviews with scores | Understand which products are popular with other customers |
| Site Owner | Easily add a new product | Make sure the online site has the latest catalogue |

<br/>

- Cart, Purchasing and Checkout

| AS A     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Shopper | Easily select the quantity and size (if applicable) of a product after adding a product to a cart | Ensure I don't accidentally select the wrong product and the quantity | 
| Shopper | The delivery information is prefilled if logged in | Smoothly proceed with my purchase | 
| Shopper | Automatically suggest to log in if I did not log in | Smoothly proceed with my purchase | 

<br/>

<div><a href="#table-of-contents">Back to top</a></div>

## Design
### Wireframes
Wireframes were created with [balsamiq](https://balsamiq.com/) and [moqups](https://moqups.com/).
You can find the wireframes [here](#).

### Brand Identity
- Vision: Excellent cocktails delivered to users through a visually appealing online store
- Mission: Provide a wide range of cocktails for guests to enjoy which can be purchased with a couple of clicks online. Be a supplier of cocktail equipment so guests can enjoy the art of cocktail making at home, without the hassle of going to a physical shops.

### Color Scheme
Color scheme is important as this is one of the first things site visitors notice when visiting the site. I chose white / black for the site's primary colors because these colors match the secondary earthy colors and make the website look professional and high-end. In addition to that, for the secondary colors of the site, I wanted to create a natural / delicate atmosphere to represent the calming sensation of flowers. For the secondary colors, I used [Coolors.co](https://coolors.co/) to create a color pallet, which you can find below.

<p align="center"><img src = "#"></p>

### Typography

- Icon: [FontAwesome](https://fontawesome.com/) is used for the main icon library accross the site.
- Favicon: I got the favicon by [Freepik](https://www.flaticon.com/authors/freepik) from [www.flaticon.com](https://www.flaticon.com/).


# Features

## Existing Features
This website is composed of 7 applications: `home`, `bag`, `checkout`, `products`, `profiles`, 'contact' and 'wishlists'

## Landing Page
The Speakeasy Landing Page or Homepage is designed as a single page website to provide site visitors with enough information so they can understand what the business is about of this site. This page has minimal amount of information to let the site visitors take next actions. The page is composed of a `Navbar`, a `Hero Image` wiht a 'Shop Now' call to action, an about section and a footer. I used the animate class to add some custom animation to the appearance of text in the hero image and about section.

### Navbar
The Navbar is fixed at the top of all pages across the site, so that the site visitors can easily navigate the whole site.  The Navbar contains the `Brand Name`, `Search Box`, `Wishlist`, `My Account Dropdown` and `Shopping Bag Icon`.
- Search box: This search box function allows the visitors to search the products on online shop with keywords. The keywords are searched over `name` and `description` field of Product Model, as well as the 'name' field of the Categories Model. (Details of these models will be described at the [Information Architecture](#information-architecture)) 
- Wishlist: Users can access their wishlist from  
- My Account Dropdown: The My Account Dropdown allows users to login, access their profile page and log out. Site owners can access the product management page to add products form here also.
- Bag Icon: The Bag Icon allows users to access their shopping bag when clicked. 


Navbar for larger screensizes (width > 992px)
<div align="center"><img src = "#" width=900></div>

Navbar for smaller screensizes (width < 992px)
<div align="center"><img src = "" width=900></div>

Navbar for authenticated users
<div align="center"><img src = "" width=900></div>



<div align="center"><img src = "" width=700></div>

### About Us Section
`About Us` section explains what the business is and the brief introduction on how to shop on the site.
<div align="center"><img src = "" width=700></div>


### Footer
The footer section consists of two sections: 1. General information about Speakeasy Cocktails and 2. Social Media icons.
1. General Info: The first footer section includes the physical address of Speakeasy Cocktails and along with a phone number and link to 'Contact Us'.

2. Social Media Icons: The Social Media icons are linked to the homepages of their respective social media sites, but in a real settting they should be linked to the businesses pages on social media.
<div align="center"><img src = "#" width=700></div>

<div><a href="#table-of-contents">Back to top</a></div>

## Product Page
### Online Shop Page
By clicking 'Shop Now' on the homepage, users are directed to the online shop or 'Products' page. This page is filtered with  by pricr rating or category using the links in the 'main navbar'. 
- Sort Filter: On the right hand side of the page or in the centre on mobile view. This allows users to filter products by price, name, category or rating if applicable.
<div align="center"><img src = "#" width=250></div>

- Result Number: It's shown above the product cards. Customers can see how many results were found in total at a glance.
<div align="center"><img src = "" width=350></div>

- Product Card: The products are displayed in cards that have `Product Name`, `Price` and 'Category' displayed below their respective images. By clicking on the product image, users are directed to the Product Details Page. If the user is logged in as a superuser, an option to Edit or Delete the item is also shown below the image on each card.

Product Card 
<div align="center"><img src = "https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/bouquet_product_card.png" width=500></div>


### Product Detail Page

- Product Image: The product image is shown on the left side of the Product Details page (product_detail.html).
- Product Information: On the right side of the product detail page, there is a `Product Name`, `Price`, `Description`, `Quantity` and `Add to Cart` button. Also for superusers, Edit / Delete option will be shown.
- Prouct Wishlist: If the user is logged in, they can use the `Add to Wishlist` button to the right of the product image in order to add the pruduct to the users wishlist. If the user is not logged in, they will be asked to register or log in to add the product to their wishlist.
- Product Review Section: Users can see the product scores and review messages by other customers. The users can leave a score from 1 to 5, and the average of the scores of the customer reviews is shown on the product page. To leave a product review, the user is asked to log in to their account or register for an account. Also, to delete a review, the customer who left the review needs to log in and the delete option will be visible next to the review after logging in. At the moment, regardless of whether they have purchase history or not, the user is able to leave a review. This is one of the features left to implement to limit it so only the user who actually purchased the product will be allowed to review.

<div align="center"><img src = "#" width=700></div>


## Shopping Bag Page
- The left side of this cart page shows the products added to the bag. Customers are able to change the quantity or remove the products in this bag page.
- On the right side of this bag page, there is an Order Summary section that shows `Bag Total`, `Delivery` and `Grand Total`. This way, customers are able to check the order summary at first glance even if they have added a lot of products to the shopping bag.

<div align="center"><img src = "#" width=700></div>

## Checkout Page
### Checkout Page
- On the checkout page, customers are asked to fill in delivery details. The delivery details will be populated automatically from the users profile if they are logged in. The billing data is also recorded in Stripe from the billing information added by the customer using a Webhook).
- Though the customer can complete the checkout process without having an account, if the customer hasn't logged in, the message "Create an account or login to save this information" is shown at the checkout page.

### Checkout Success Page
- A thank you message will be displayed after the checkout process as well as the table that holds the order details, users will be imfored via toast message that a confirmation email has been sent to the email address that they provided.
- A `Keep Shopping` button is placed at the end of the page, and if the customer has been logged into their account, `Back to Profile` will be shown.

<div><a href="#table-of-contents">Back to top</a></div>

## Wishlist Page

- If a user is registered and logged in, they can add products to their wishlist to view later. The wishlist is accessed by a heart icon at the top right of the main nav bar in desktop view and in the dropdown menu in mobile view. 
- The Wishlist Page mirrors the All Products Page however only items added by the user are displayed. Each Product Card displays the same information as cards on the Products Page and allows users to click in the product's product details page via the product's image


<div align="center"><img src = "#" width=700></div>


## Profiles Page
`My Profile` page is available for authenticated users and will be shown in the `My Account` Dropdown menu at the navbar which appears when you log into your account.
### My Profile Page
- In Profile Page, authenticated users can 1. edit `Delivery Information` and 2. see `Order History`.

## Admin Product Managment
Only authenticated superusers can access the admin page (1.products/add/, 2. products/edit/, 3. products/delete/, 4. 5. 6. ). If non-logged in users try to access the url directly, it will redirect to the sign in page. If a non-superuser tries to access the url, an error message pops up which says that only a superuser can access this page.

## Contact Page

A simple contact form is placed at the end of the landing page. The email address field is prefilled if the users are logged into their account. Site visitors will fill out fields `name`, `email`, `subject` and `message` when they submit the form. An email with the inquiry from the form will be sent to the admin of the website (handling by django send_mail() functionality).
<div align="center"><img src = "" width=700></div>
## Django-allauth features
Base template for allauth has `Back to Home` button at the end of the page, for easy navigation for users.
- Sign Up: The users will be asked to fill out `E-mail`, `User Name` and `Password` to create an account. When the sign up form is submitted, a verification email will be sent to the user's email address to complete the sign up process.
- Log In: Users will be asked to input `User Name` or `Email`, and `Password` to login. If the user successfully logged in, a success message will pop up and redirect to the landing page.
- Log out: Log out page is accessible from the site menu. After the user successfully signed out button on the sign out page, a success message will appear and redirect to the landing page.
- Forgot password: Forgot password page is accessible from Sign In page. Users will be asked to put in an email address which they have used for their registration to the site. An email with a link to reset the password will be sent after submitting the form.

<div><a href="#table-of-contents">Back to top</a></div>

