# Speakeasy Cocktails
## Code Institute - Milestone 4 Project

<div align="center"><img src = "https://github.com/d-mcalpin/speakeasy/blob/master/readme_material/speakeasy_mockup.png" width=700></div>

### Live Heroku Link:

[Speakeasy Cocktails](https://speakeasy-cocktails.herokuapp.com/)

# Table of Contents

- <a href="#aim">1. Aim Of The Site </a>
- <a href="#scope">2. Scope </a>
- <a href="#users">3. User Stories</a>
- <a href="#structure">4. Structure </a>
- <a href="#future">5. Future Features </a>
- <a href="#info">6. Information Architecture </a>
- <a href="#skeleton">7. Skeleton </a>
- <a href="#surface">8. Surface </a>
- <a href="#tech">9. Technologies Used </a>
- <a href="#testing">10. Testing </a>
- <a href="#deployment">11. Deployment </a>
- <a href="#credits">12. Credits </a>

## Summary
Speakeasy Cocktails is an online coctail retailer, which specialises in delivering ready to drink cocktails and bar equipment direct to your home.

<span id="aim"></span>

## 1. Aim of the Site

Finding delicious cocktails can sometimes be tricky, particularly if you have to make them yourself.

The aim of the Speakeasy Cocktails website is to make this process finding great cocktails and enjoying them at home an easy and pleasant experience. On each product page, customers have the opportunity to read reviews about the cocktails and equipment that is for sale as well as the opportunit to add products to a wishlist in case they would like to try them in the future.

Products are displayed in an easy to use format where customers can search by keyword or find an item by category from anywhere on the site.

<span id="scope"></span>

## 2. Scope

Speakeasy Cocktail's primary target market is cocktail enthusiasts. We hope to encourage frequent purchases by offering customers an easy to use interface and a pleasant experience, while the ability to leave reviews may encourage customers to share knowledge and opinions with other customers. 

### Project Goals
#### Target Audience
- People who are looking to buy cocktails and cocktail equipment
- People who unique and traditional cocktails
- People who want to try to make a cocktails at home by purchasing equipment by themselves
- People who want to read reviews about cocktails that have been left by other users

#### Visitor / User Goals
- Purchase products in a smooth and secure way
- Get informed with the products before buying by reading product reviews / product information
- Inform other customers by leaving my own reviews
- Add products to my wishlist so that I can order them in the future

#### Business Goals (Site Owner's Goals)
- Provide customers with a secure and safe ecommerce shop
- Establish the shop's brand image
- Expand their business effectively
- Make profit from selling products / services

<div><a href="#table-of-contents">Back to top</a></div>

<span id="users"></span>

## 3. User Stories

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

- Products annd Online shopping

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

<div><a href="#table-of-contents">Back to top</a></div

<span id="structure"></span>

## 4. Structure
This website is composed of 7 applications: `home`, `bag`, `checkout`, `products`, `profiles`, 'contact' and 'wishlists'

### Homepage
The Speakeasy Homepage is designed as a single page website to provide site visitors with enough information so they can understand what the business is about of this site. This page has minimal amount of information to let the site visitors take next actions. The page is composed of a `Navbar`, a `Hero Image` wiht a 'Shop Now' call to action, an about section and a footer. I used the animate class to add some custom animation to the appearance of text in the hero image and about section.

#### Navbar
The Navbar is fixed at the top of all pages across the site, so that the site visitors can easily navigate the whole site.  The Navbar contains the `Brand Name`, `Search Box`, `Wishlist`, `My Account Dropdown` and `Shopping Bag Icon`.
- Search box: This search box function allows the visitors to search the products on online shop with keywords. The keywords are searched over `name` and `description` field of Product Model, as well as the 'name' field of the Categories Model. (Details of these models will be described at the [Information Architecture](#information-architecture)) 
- Wishlist: Users can access their wishlist from  
- My Account Dropdown: The My Account Dropdown allows users to login, access their profile page and log out. Site owners can access the product management page to add products form here also.
- Bag Icon: The Bag Icon allows users to access their shopping bag when clicked. 


Navbar for larger screensizes (width > 992px)
<div align="center"><img src = "https://github.com/d-mcalpin/speakeasy/blob/master/readme_material/navbar_signedout.PNG" width=900></div>

Navbar for smaller screensizes (width < 992px)
<div align="center"><img src = "https://github.com/d-mcalpin/speakeasy/blob/master/readme_material/mobile_navbar.PNG" width=500></div>

Navbar for authenticated users
<div align="center"><img src = "https://github.com/d-mcalpin/speakeasy/blob/master/readme_material/navbar_signedin.PNG" width=900></div>



#### About Us Section
`About Us` section explains what the business is and the brief introduction on how to shop on the site.
<div align="center"><img src = "https://github.com/d-mcalpin/speakeasy/blob/master/readme_material/about_use.PNG" width=700></div>


#### Footer
The footer section consists of two sections: 1. General information about Speakeasy Cocktails and 2. Social Media icons.
1. General Info: The first footer section includes the physical address of Speakeasy Cocktails and along with a phone number and link to 'Contact Us'.

2. Social Media Icons: The Social Media icons are linked to the homepages of their respective social media sites, but in a real settting they should be linked to the businesses pages on social media.

<div align="center"><img src = "https://github.com/d-mcalpin/speakeasy/blob/master/readme_material/footer.PNG" width=700></div>

<div><a href="#table-of-contents">Back to top</a></div>

### Product Page

#### Online Shop 
By clicking 'Shop Now' on the homepage, users are directed to the online shop or 'Products' page. This page is filtered with  by pricr rating or category using the links in the 'main navbar'. 
- Sort Filter: On the right hand side of the page or in the centre on mobile view. This allows users to filter products by price, name, category or rating if applicable.
<div align="center"><img src = "https://github.com/d-mcalpin/speakeasy/blob/master/readme_material/products_sort.PNG" width=700></div>

- Result Number: It's shown above the product cards. Customers can see how many results were found in total at a glance.

- Product Card: The products are displayed in cards that have `Product Name`, `Price` and 'Category' displayed below their respective images. By clicking on the product image, users are directed to the Product Details Page. If the user is logged in as a superuser, an option to Edit or Delete the item is also shown below the image on each card.

#### Product Card 
<div align="center"><img src = "https://github.com/d-mcalpin/speakeasy/blob/master/readme_material/product_card.PNG" width=300></div>


### Product Detail Page including Reviews

- Product Image: The product image is shown on the left side of the Product Details page (product_detail.html).
- Product Information: On the right side of the product detail page, there is a `Product Name`, `Price`, `Description`, `Quantity` and `Add to Cart` button. Also for superusers, Edit / Delete option will be shown.
- Product Wishlist: If the user is logged in, they can use the `Add to Wishlist` button to the right of the product image in order to add the pruduct to the users wishlist. If the user is not logged in, they will be asked to register or log in to add the product to their wishlist.
- Product Review Section: Users can see the product scores and review messages by other customers. The users can leave a score from 1 to 5, and the average of the scores of the customer reviews is shown on the product page. To leave a product review, the user is asked to log in to their account or register for an account. Also, to delete a review, the customer who left the review needs to log in and the delete option will be visible next to the review after logging in. At the moment, regardless of whether they have purchase history or not, the user is able to leave a review. This is one of the features left to implement to limit it so only the user who actually purchased the product will be allowed to review.

<div align="center"><img src = "https://github.com/d-mcalpin/speakeasy/blob/master/readme_material/product_details.PNG" width=700></div>


### Shopping Bag Page
- The left side of this cart page shows the products added to the bag. Customers are able to change the quantity or remove the products in this bag page.
- On the right side of this bag page, there is an Order Summary section that shows `Bag Total`, `Delivery` and `Grand Total`. This way, customers are able to check the order summary at first glance even if they have added a lot of products to the shopping bag.

<div align="center"><img src = "https://github.com/d-mcalpin/speakeasy/blob/master/readme_material/shopping_bag.PNG" width=700></div>

### Checkout Page
#### Checkout Page
- On the checkout page, customers are asked to fill in delivery details. The delivery details will be populated automatically from the users profile if they are logged in. The billing data is also recorded in Stripe from the billing information added by the customer using a Webhook).
- Though the customer can complete the checkout process without having an account, if the customer hasn't logged in, the message "Create an account or login to save this information" is shown at the checkout page.

<div align="center"><img src = "https://github.com/d-mcalpin/speakeasy/blob/master/readme_material/checkout.PNG" width=700></div>

#### Checkout Success Page
- A thank you message will be displayed after the checkout process as well as the table that holds the order details, users will be imfored via toast message that a confirmation email has been sent to the email address that they provided.
- A `Keep Shopping` button is placed at the end of the page, and if the customer has been logged into their account, `Back to Profile` will be shown.

<div><a href="#table-of-contents">Back to top</a></div>

### Wishlist Page

- If a user is registered and logged in, they can add products to their wishlist to view later. The wishlist is accessed by a heart icon at the top right of the main nav bar in desktop view and in the dropdown menu in mobile view. 
- The Wishlist Page mirrors the All Products Page however only items added by the user are displayed. Each Product Card displays the same information as cards on the Products Page and allows users to click in the product's product details page via the product's image


<div align="center"><img src = "https://github.com/d-mcalpin/speakeasy/blob/master/readme_material/wishlist.PNG" width=700></div>


### Profiles Page
The`My Profile` page is available for authenticated or logged in users and will be shown under the `My Account` Dropdown menu non the navbar.

#### My Profile Page
- On the Profile Page, authenticated users can 1. Edit `Delivery Information` and 2. View their `Order History`.

<div align="center"><img src = "https://github.com/d-mcalpin/speakeasy/blob/master/readme_material/profile.PNG" width=700></div>

### Admin Product Managment
The Product Management link allows authenticated superusers can access the `Add Product` page. Here an administrator of the site can add new products to the site. When logged in as an admin or superuser, the user can also edit or delete products from the Products or Product Details Pages. If non-logged in users try to access the url directly, it will redirect to the sign in page. If a non-superuser tries to access the url, an error message pops up which says that only a superuser can access this page.

<div align="center"><img src = "https://github.com/d-mcalpin/speakeasy/blob/master/readme_material/product_management.PNG" width=700></div>

### Contact Page

A simple contact form is accessible by a link in the product navigation bar or by clicking `Contact Us` in the footer. Site visitors will fill out fields `name`, `email`, `subject` and `message` when they submit the form. An email with the inquiry from the form will be sent to the admin of the website (handling by django send_mail() functionality).


## Django-allauth features
Base template for allauth has `Back to Home` button at the end of the page, for easy navigation for users.
- Sign Up: The users will be asked to fill out `E-mail`, `User Name` and `Password` to create an account. When the sign up form is submitted, a verification email will be sent to the user's email address to complete the sign up process.
- Log In: Users will be asked to input `User Name` or `Email`, and `Password` to login. If the user successfully logged in, a success message will pop up and redirect to the landing page.
- Log out: The Log Out Page is accessible from the site menu. After the user successfully signs out by clicking the button on the sign out page, a success message will appear and redirect to the home or landing page.
- Forgot password: Forgot password page is accessible from Sign In page. Users will be asked to put in an email address which they have used for their registration to the site. An email with a link to reset the password will be sent after submitting the form.

<div><a href="#table-of-contents">Back to top</a></div>

<span id="future"></span>

## 5. Future Features

### Ratings on Products Page
I would like to add each product's star rating to the product card on the products page however this would be outside the scope of this project.

### Multiple Wishlists
For the most part, one wishlist should be sufficient for users. However, there may be cases in which customers would like to organise products into various wishlists. For example, if a customer would like a wishlist for presgiftent ideas or unique wishlists for different occasions, I would like to provide them with this ability.

### Customer Service Chatbot
Customers are invited to email if they have any queries or issues with their orders. In instances where customers have queries that could be dealt with quickly and in real-time, I would like to investigate the practicality of a chatbot. This could improve the user experience and save them time as they would not have to partake in a back-and-forth email chain. 

<span id="info"></span>
## 6. Information Architecture

### Database Choice
While this project was in development, it utilised the SQLite3 database, but once deployed to Heroku, a PostgresSQL database was used.

### Schema Design
Looking at the requirements of the project and the site that was planned, it was determined that five main models were required. 

The main models are: Products, Profiles, Reviews, Orders, and Wishlists. Models that act to support and work in tandem with these included OrderLineItem, Categories, and WishlistLineItem. 

![Database Schema](https://github.com/d-mcalpin/speakeasy/blob/master/readme_material/speakeasy_schema.PNG)

<div><a href="#table-of-contents">Back to top</a></div>
<span id="skeleton"></span>

## 7. Skeleton

###  Wireframes

Wireframes were created with [balsamiq](https://balsamiq.com/).

The [Speakeasy Desktop Wireframes are available here](https://drive.google.com/file/d/1dMScUY5iQfrQNF4l2grG6s0qgkEGP5yw/view?usp=sharing)  and the [Speakeasy Mobile Wireframes are available here](https://drive.google.com/file/d/1nyUIpmPiKz06-oXt08thrQOAQidN4RMB/view?usp=sharing) .

<span id="surface"></span>

## 8. Surface
### Fonts
The Google Font, Lato is used across the site as the most prominent font. It was chosen as it is very legible, even in paragraphs with text, and it works well across web and mobile devices.

### Brand Identity
- Vision: Excellent cocktails delivered to users through a visually appealing online store
- Mission: Provide a wide range of cocktails for guests to enjoy which can be purchased with a couple of clicks online. Be a supplier of cocktail equipment so guests can enjoy the art of cocktail making at home, without the hassle of going to a physical shops.

### Colour Scheme
The colorr scheme is important as this is one of the first things site visitors notice when visiting the site. I chose a blue, teal, white and black scheme for the site's primary colors because they make the website look professional and high-end. I used [Coolors.co](https://coolors.co/) to create a colour pallet, which you can find below.

<p align="center"><img src = "https://github.com/d-mcalpin/speakeasy/blob/master/readme_material/speakeasy_palette.png"></p>

### Typography

- Icon: [FontAwesome](https://fontawesome.com/) is used for the main icon library accross the site.
- Favicon: I got the Martini favicon from the site [Freepik](https://www.flaticon.com/authors/freepik) and [www.flaticon.com](https://www.flaticon.com/).

### Defensive Design
- The following defensive programming design elements are in place to prevent a negative user experince:
    - Toast Messaging is used to prevent users from accessing areas of the site that they do not have authorisation for. 
    - If no images are available for products, a default image will appear instead to prevent no image being shown.
    - If a user encounters a 404 or 500 error, a custom error page will appear, offering to return users to the products page.

<div><a href="#table-of-contents">Back to top</a></div>

<span id="tech"></span>

## 9. Technologies Used

### Languages 
HTML & CSS were used for the basic site structure and styling 

JavaScript was used to further enhance the user's experience. For example, it is used to update the customer's grand total in real time if they use loyalty points to discount their purchase, to display a spinner if a page is taking a while to load, and to return the user to the top of the page when scrolling.

Python was used to handle data procured from the database.

### Frameworks and Libraries
[Django](https://www.djangoproject.com/) was used to develop the project, taking advantage of certain in-built elements such as authentication as well as its templating language, display variables and data handling.

[Bootstrap](https://getbootstrap.com/) was used to create interactive and visual elements such as the dropdown elements, and the site's general responsive design.

[Animate](https://animate.style/) was used for some styling elements on the homepage, index.html

### Tools
[PIP](https://pip.pypa.io/en/stable/) was used to install and manage software packages.

[Git](https://git-scm.com/) was used to track changes in code during development.

[GitHub](https://github.com/) was used to host the project’s repository.

[Heroku](https://heroku.com/) was used to ultimately deploy the live website.

[Stripe](http://stripe.com/) was used to accept payments via the checkout app.

[Amazon Web Services](https://aws.amazon.com/) was used to host images and static files for the deployed website. 

[DB Designer](https://www.dbdesigner.net/) was used to design the schema that this site would utilise for its database.

[Balsamiq](https://balsamiq.com/) was used to create the wireframes that the site's layout is based upon.

[Coolors](https://coolors.co/) was used to help find a suitable palette for the site and to check if colours might work together.

[Google Fonts](https://fonts.google.com/) was used to find the fonts that would be suitable as headings and general text content.

[Font Awesome](https://fontawesome.com/) was used to find icons for use in buttons across the site.

[Code Beautify](https://codebeautify.org/) was used to format HTML files and ensure consistency in spacing.

[Google Drive](www.google.com) was used to store and share the projects Wireframes.

[CSS Autoprefixer](https://autoprefixer.github.io/) was used to add multiple browser webkits to CSS.

<span id="testing"></span>

## 10. Testing

The testing process, issues encountered, and any known issues can be found in the [testing.md](https://github.com/d-mcalpin/speakeasy/blob/master/TESTING.md) file.

<div><a href="#table-of-contents">Back to top</a></div>
<span id="deployment"></span>

## 11. Deployment

### Local Deployment
If you would like to explore or further develop this project locally, you can clone it and deploy it locally:

* Navigate to the [Speakeasy project repository](https://github.com/d-mcalpin/speakeasy)

* Click on the button marked "Code"

* Copy the link provided (https://github.com/d-mcalpin/speakeasy.git)

* As this project uses Python, it is best to operate within a virtual environment. The instructions on setting up and activating a virtual environment may be different, depending on your operating system. The official Python Documentation would be the best place to consult in order to set this up correctly.

* To install the required modules used by this project, use the command "pip -r requirements.txt"

* Add environment variables for:
    * SECRET_KEY
    * STRIPE_PUBLIC_KEY
    * STRIPE_SECRET_KEY
    * STRIPE_WH_SECRET
    * DATABASE_URL

* These variables can be added to Gitpod's settings, if using Gitpod, or to an env.py file. If using an env.py file, make sure it is added to .gitignore to ensure that all secret keys are kept secret.

* To set up the SQLite3 database for the first time, use the following commands in your terminal
```
python3 manage.py makemigrations
python3 manage.py migrate
```

* Create a superuser with the command

```
python3 manage.py createsuperuser
```

* You can run the cloned application to ensure that all is working correctly

```
python3 manage.py runserver
```

To load product, category, and mechanics data, type the following command into the terminal, specifying which fixture you would like to load. Be sure to load categories and mechanics before products.

```
python3 manage.py loaddata fixture_name
```

### Heroku Deployment
* Navigate to https://dashboard.heroku.com/ and sign in / register for an account
* Click on "New" in the top right corner and select "Create new app"
* Select a unique app name and choose a region that is local
* On the resources tab, search for Heroku Postgres and add as an add-on
* Navigate to the app's settings page and and click on the 'Reveal Config Variables' button
* Add environment variables for:
    * SECRET_KEY
    * STRIPE_PUBLIC_KEY
    * STRIPE_SECRET_KEY
    * STRIPE_WH_SECRET
    * DATABASE_URL
* Freeze the app's required modules in the terminal
```
pip3 freeze > requirements.txt
```
* Create a Procfile
```
echo web: gunicorn speakeasy.wsgi:application > Procfile
```
* Set up the database to work with Postgres. To start, we have to comment out the current DATABASE settings (in our project's settings.py file) and add

```
DATABASES = {
        'default': dj_database_url.parse(database_url_from_heroku_config_vars)
        }
```
* Run all migrations 
```
python3 manage.py makemigrations
python3 manage.py migrate
```
* Create a superuser
```
python3 manage.py createsuperuser
```
* Navigate back to settings.py once this is complete and restore the original database settings.
* Add an if statement to the database settings to check if 'DATABASE_URL' in os.environ and to use the Postgres database if so (remembering to get the URL from your environment settings rather than pasting in the URL directly) 
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
        }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```
* Log in to Heroku from your terminal and temporarily disable collect static
```
heroku login -i
heroku config:set DISABLE_COLLECTSTATIC=1 --app APP_NAME
```
* In settings.py, add the Heroku app to the list of ALLOWED_HOSTS. Having localhost in this list ensures that GitPod can still get access.
* It is possible to set up Heroku to deploy automatically from Github by navigating to the Deploy section on the app's dashboard and scrolling down to Deployment method. 
* Select GitHub and connect to the relevant repository
* Once connected, you can enable Automatic Deploys so that each push to the master branch (or other chosen branch) will result in Heroku deploying a new version of the app.

### Utilising Amazon Web Services
* Navigate to [Amazon Web Services]() and crete or sign into an account
* Search for S3 or find it through the services menu
* Create a new bucket and give it the same name as Heroku app (this is to make it easier to organise more than anything)
* Uncheck block all public access and conclude creating bucket
* In the bucket's properties tab, edit static web hosting and set default values for index and error document.
* Open the permissions tab and edit Cross-origin resource sharing (CORS)
* Paste in the following
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
* Select "Policy Generator" to create a new security policy
* Select S3 Bucket Policy as the policy type and add * to Principal in order to allow all principals
* Set Action to GETobject and paste in the Amazon Resource Name from the Edit Bucket Policy tab. It will be in the format
```
arn:aws:s3:::bucket
```
* Click add statement
* Click Generate Policy
* Copy policy and paste into bucket policy editor
* Before clicking save, add a /* to the end of the "Resource" value as we want to allow access to all resources in this bucket
* In the Access Control List (ACL), set list objects permission for everyone

* Next we need to create a user to access this bucket. We can do this through the Identity and Access Management (IAM) service.
* Create a group and give it a new name. The steps of attaching policy can be skipped for the moment.
* Create a policy by navigating to the policies tab and selecting create policy
* From the JSON tab, select Import Managed Policy
* Search for S3 and then import S3 Full Access Policy
* On S3 itself, select your bucket and copy the ARN. Paste this into the Resource item as follows:
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::bucket",
                "arn:aws:s3:::bucket/*"
            ]
        }
    ]
}

```

* Click Review Policy
* Give it a name and description, and create policy
* Attach this policy to your group by clicking on groups, the name of your created group, permissions, attach policy
* Search for the created policy, select it, and click Attach Policy
* Now create a user by navigating to Users tab and selecting Add User
* Give it a name and give programmatic access
* Add user to group and click through to the end to create the user
* Download the .csv file, which contains the user's access key and secret access key

* To connect Django to S3, we need two packages, boto3 and django-storages
* Add storages to installed apps in settings.py
* Add AWS keys to Heroku's config vars
* Add if statement to settings.py to check for USE_AWS environment variable
```
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'speakeasy-cocktails'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```
<div><a href="#table-of-contents">Back to top</a></div>

<span id="credits"></span>

## 12. Credits

### Content
The design and style of my project inlcuding README and TESTING files were initially inspired by elements of the following project:
- [mark-obeirne's Milestone 4 Project, Boardgame Empire ](https://github.com/mark-obeirne/boardgameempire/)

Some project content as well as the README and TESTING files were inspired by the following project:
- [AsunaMasuda's Milestone 4 Project, FloweryDays](https://github.com/AsunaMasuda/FloweryDays)

The following sources were used for code snippets or inspiration throughout the project:

- Initial instructions for setting up the site were taken from the E-Commerce Site walkthrough from the [Code Institute](https://codeinstitute.net/) Full Stack Developer Course.
- Advice on centering Bootstrap columns was taken from the following [Stakoverflow Thread](https://stackoverflow.com/questions/23682876/centering-the-row-in-bootstrap-with-a-minimum-width)
- Direction for keeping the footer at the bottom of the page was taken from this [Stackoverflow Thread](https://stackoverflow.com/questions/36990624/back-to-top-button-and-footer-positioning)
- Implementation of the Wishlist feature in Django was taken from this [Stackoverflow Thread](https://stackoverflow.com/questions/61561263/django-wishlist-feature-implementing)
- Advice on responsive design and implementing AWS was taken from Code Institute Tutor Support.
- Integration of the Reviews section of the product page and Wishlist was advised by my mentor, Oluwafemi Medale

### Media

**Images**
- The homepage image was downloaded from Taryn Elliott's collection of Pexels, available [here](https://www.pexels.com/@taryn-elliott)
- The product images were sourced from Alexa_Fotos and other collections on Pixabay: [Available Here](https://pixabay.com/users/alexas_fotos-686414/?tab=about)
 
 
**Fonts and Icons**
- Fonts are from [Google Fonts](https://fonts.google.com/) and icons from [Font Awesome](https://fontawesome.com/)

**Mockups**
- Mockups were generated using [ami.responsivedesign.is](ami.responsivedesign.is)
    

### Acknowledgements
- **Oluwafemi Medale** (My Mentor) - Thank you for your assistance with this project.
- **The Code Institute Slack Community** - The community was a great source of inspiration and assistance throughout the project.
- **My Family** for their assistance testing the website and adding reviews.
- **Code Institute's Student Support** for their assistance throughout this project.

### Disclaimer
I do not own any of the text written for the individual reviews. All opinions are that of their owners and not of the website. Please contact me in case of any copyright issue and I will happily remove anything.

This project is for educational purposes only.

***
<div><a href="#table-of-contents">Back to top</a></div>