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

## Background

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

### Brand Logo
Logo design is the cornerstone in your brand identity and presents a company's name, product and brand. I used [Canva](https://www.canva.com/en_gb/) to create the brand logo file. The font represents the brand value `elegance` and the image of a branch at the top was added to represent `Nature` brand value.
<p align="center"><img src = ""></p>

<div "text-align: right;"><a href="#table-of-contents">Back to top</a></div>

# Features

## Existing Features
This website is composed of 7 applications: `home`, `bag`, `checkout`, `products`, `profiles`, 'contact' and 'wishlists'

## Landing Page
The Speakeasy Landing Page or Homepage is designed as a single page website to provide site visitors with enough information so they can understand what the business is about of this site. This page has minimal amount of information to let the site visitors take next actions. The page compose of `Navbar`, `Carousel`, `About`, `Why Choose Us?`, `testimonials` and `Contact Form` section. As scrolling down on thie page, the elements are smoothly being placed by [Animate.css](https://animate.style/) and [wow.js](https://wowjs.uk/docs) animation effects to give a dynamic and sophisticated experience to the site visitors.

### Navbar
Navbar is fixed at the top of pages across the site, so that the site visitors easily navigate the whole site.  Navbar contains  `Brand Logo`, `Search Box`, `Site Menu`, `My Account dropdown` and `Cart icon`.
- Search box: This search box function allows the visitors to search the products on online shop with keywords. The keywords are searched over `name` and `descriotion` field of Product Model, `name` field of Color Model and `name` field of Flower Model.(Details of these models will be described at the [Information Architecture](#information-architecture)) This function uses "OR" condition not "AND" when searching the keywords, meaning, if the search query was "Tulip Rose", the search result shows the product found using the keyword "Tulip" OR "Rose". Searching with "OR" condition is chosen in order not to limit the possibilities for the products the potential customers want to purchase.
- Site Menu & My Account dropdown: The site menu collapses to toggle icon less than 992px width. My Account dropdown is included to toggle menu for smaller screen.
- Cart icon: The number next to the cart icon shows the total of items added to the cart.


Navbar for larger screensizes (width > 992px)
<div align="center"><img src = "#" width=900></div>

Navbar for smaller screensizes (width < 992px)
<div align="center"><img src = "" width=900></div>

Navbar for authenticated users
<div align="center"><img src = "" width=900></div>



<div align="center"><img src = "" width=700></div>

### About Us & Why Choose Us?
`About Us` section explains what the business is and the brief introduction on how to shop on the site.
<div align="center"><img src = "" width=700></div>

`Why Choose Us?` section showcases three sales points of the shop with icons representing each one.

<div align="center"><img src = "" width=700></div>


### Contact Form
A simple contact form is placed at the end of the landing page. The email address field is prefilled if the users are logged into their account. Site visitors will fill out fields `name`, `email`, `subject` and `message` when they submit the form. An email with the inquiry from the form will be sent to the admin of the website (handling by django send_mail() functionality).
<div align="center"><img src = "" width=700></div>

### Footer
The footer section consists of two sections: 1. General information of the Shop and Quick Link, 2. Social Media icons.
1. General Info and Quick Links: The first footer section includes the shop address and its opening hours and quick links to the pages within the site.
<div align="center"><img src = "" width=700></div>