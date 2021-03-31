# Testing - Speakeasy Cocktails
## Table of Contents

1. [Manual Testing](#manual-testing)
    - [Responsiveness](#responsiveness)
    - [Home Page](#home-page)
    - [Navbar](#navbar)
    - [Footer](#footer)
    - [Onlineshop and Products](#onlineshop-and-products)
    - [Reviews](#reviews)
    - [Shopping Bag](#bag)
    - [Checkout and Checkout Success Page](#checkout-and-checkout-success-page)
    - [SignIn and Order History](#signin-and-order-history) 
    - [Profile and Order History](#profile-and-order-history) 
    - [Admin Product Management](#admin-product-management) 
    - [Bugs](#bugs)

2. [Code Validation and Formatting](#code-validation-and-formatting )
    - [Validation Tools](#validation-tools)
    - [Formatter](#formatter)

3. [Compatibility and Responsiveness](#compatibility-and-responsiveness)

# Manual Testing
These tests were conducted on the deployed site on Heroku.

## Responsiveness
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Site User/ Shopper | access the website with any devices | Use the website anytime and anywhere |
| Shopper | All the important services are accessible from nav bar| Don't need to scroll to find important information | 
| Shopper | Have a shopping bag icon on nav bar | Always check the current order and checkout when I want | 
### Test conducted:
- Access each page in the site with different screen sizes with Google Dev Tool's Emulator and check the layout and format of site elements
### Result:
- Navbar: I have the search bar collapsed for smaller than medium screen size (width < 992px) because the search bar with input field conflicted with other navbar components. 
'My Account' pulldown list is included to toggle menu for smaller than medium screen size.
### Verdict:
Passed all tests.

## Home Page
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Shopper | Easily see what services are offered | Find the service I want to use |
### Test conducted:
- Click all the buttons and links on the page
### Result:
- All the buttons and links are working as expected. 
### Verdict:
Passed all tests.


## Navbar
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- | 
| Shopper | Have a shopping bag icon on nav bar | Always check the current order and checkout when I want |  
### Test conducted:
- Click the menu links and see if all the links work properly.
- Change the screensizes and check if the menu and the keyword search get collapsed not to overwrap each other.
### Result:
- The items on the navbar do not overwrap with the common screensizes.
### Verdict:
Passed all tests.

## Footer
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Shopper | Easily see what services are offered | Find the service I want to use |
### Test conducted:
- Click all the links to see it they work as expected.
- Click the social media icons to see if the links work as expected.
- The layout changes upon different screen sizes.
### Result:
- All working fine
### Verdict:
Passed all tests.

## Contact Form
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Shopper | Contact the site owners | Find out more about products |
### Test conducted:
- Submit the contact form to see if the admin receives an email.
### Result:
- The email was sent after submitting the contact form.
### Verdict:
Passed all tests.

## Online Shop and Products
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Shopper | Search a product with keywords | Find the most appropriate products |  
| Shopper | View individual product pages that have prices, descriptions, sizes, etc | Get detailed information about the product before purchasing | 
| Shopper | Filter with a specific category of product | Easily find products in a specific category | 
| Shopper/Site Owner | Leave/View product reviews with scores | Understand which products are popular by the other customers | 
### Test conducted:
- Use various keywords in keyword search and check if it works as expected.
- Check if the products page / the individual product page is displayed without breaking the layout for common screensizes.
- Navigations such return to previous page button etc don't break accessing by different paths.
- Check if the quantity counter works as expected and gives an informative error message if the number is outside of the range (1-99).
### Result:
- The layout of the Product Details page for screens less than 992px was slightly too large. It was fixed by changing the appropriate bootstrap grid system.
### Verdict:
Passed all tests.

## Reviews
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Site User | Read reviews left by other users | Make informed decisions purchasing products | 
| Site User | Post and delete reviews about products | Inform other customers about the quality of my purchases | 
| Site Owner | Delete any inappropriate comments| Control what users are posting | 
### Test conducted:
- Attempted to post a review as a non authenticated user.
- Posted a review as an authenticated user.
- Deleted a review as a user and superuser.
### Result:
- All reviews were posted and deleted successfully.
### Verdict:
Passed all tests.

## Wishlists
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Site User | Add products to my wishlist | View the products later | 
| Site User | View products in my wishlist | Decide if I want to buy them or delete them from my wishlist | 
### Test conducted:
- Added an item to my wishlist as an authenticated user.
- Viewed my wishlist via the icon in the Navbar
- Deleted a product from my wishlist.
- Deleted my entire wishlist
### Result:
- All wishlist items were posted and deleted successfully.
### Verdict:
Passed all tests.

## Shopping Bag
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Shopper | Easily select the quantity and size (if applicable) of a product after adding a product to a cart | Ensure I don't accidentally select the wrong product and the quantity | 
### Test conducted:
- Checked if the quantity counter works properly and gives an error message if the number is out side of the range (1-99).
- Checked if the Remove/Update link works properly.
### Result:
- The quantity counter works as expected.
- Remove/Update link works as expected.
### Verdict:
Passed all tests.

## Checkout and Checkout Success Page
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- |  
| Shopper | The delivery information is prefilled if logged in | Smoothly proceed with my purchase | 
| Shopper | Automatically suggest to log in if I did not log in | Smoothly proceed with my purchase | 
### Test conducted:
- Access the checkout page after adding some items to the cart with/without logging in.
- Complete the check out process with various type of products from different categories.
### Result:
- The delivery information form is prefilled if logged in.
- If not logged in, a message appears at the end of the form: "Create an account or login to save this information".
- All the webhooks in Stripe returned success after the checkout.
- The customer received the order confirmation email to the email address that was added to the checkout page.
### Verdict:
Passed all tests.

## Sign In and Order History
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Site User | Receive an email confirmation after registering | Verify that my account registration was successful |
| Site User | Easily register for an account | Have a personal account and be able to view my profile and ability to check order history |
| Site User | Easily recover my password in case I forget it | Recover access to my account |
### Test conducted:
- Sign up with an email and check if the account receives an email and Log in with the created account.
- Use `forgot password?` link to check if recovering the password works.
### Result:
- Email Address Confirmation email contains `site_name` and `site_domain` and they returned the default value 'example.com'. These were changed to the deployed site `speakeasy-cocktails.herokuapp.com/` in Django Admin > Sites.
- The font color of the submit button on Password Reset page was set as the same color as the back ground. It was fixed after this test.
### Verdict:
Passed all tests.

## Profile and Order History
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Easily register for an account | Have a personal account where I can edit my information |  
| Site User | View my order history | Purchase the same product again in the next order |
### Test conducted:
- Create a new account and edit the delivery information.
- Order History Page renders as expected accessing from My Account page.
### Result:
- Delivery information is updated as expected after changing on the My Profile page.
- The Order History rendered correctly.
### Verdict:
Passed all tests.

## Admin Product Management
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Site Owner | Easily add a new product | Make sure the online site has the latest lineups | 
| Site Owner | Easily edit a new product | Manage products posts easily on the website | 
### Test conducted:
- Add a product with/without image and check if they are created successfully.
- If the user is not superuser and accessed to the direct url to Admin Product, they get redirected and informed.
### Result:
- The rating option was included to the add product form. I deleted this because reviews are not needed when adding a new product.
- Unauthorised users get redirected to the home page and get information on the toast.
### Verdict:
Passed all tests.

## Bugs
- Although the scroll to top button works on the Products Page, it's functionality is inhibited when it reaches the footer of the page. This is a bug that is still to be fixed when time allows.
- I wanted to add the User Review Star Ratings to the individual product cards on the Products page however the actual rating would not appear for each individual product, this has been removed pending further investigation.


## LightHouse on Google DevTool
I used Lighthouse by Google on https://speakeasy-cocktails.herokuapp.com/. Lighthouse returned a poor performance score based on the loading times of third party elements however SEO and best practices scored high"
<br>Result: <div align="center"><img src = "https://github.com/d-mcalpin/speakeasy/blob/master/readme_material/lighthouse_speakeasy.PNG" width=700></div>


# Code Validation and Formatting 
### Validation Tools
I used these validation tools below for each file.
- HTML: [W3C HTML Validator](https://validator.w3.org/) *For HTML validator, I passed each URI directly to the validator since the html files contain Django templates.
- CSS: [W3C CSS validator](https://jigsaw.w3.org/css-validator/)
- JavaScript: [JSHint](https://jshint.com/)
- Python: [PEP8 online](http://pep8online.com/)

Result:
- HMTL: In the W3C HTML Validator, there is an error Duplicate ID when as the mobile header and main header use the same id. However these will never be used at the same time.
- CSS: The W3C CSS Validator showed up library errors for Animate and Bootstrap however these relate to external libraries and not the projects CSS.
- Javascript: JSHint passed without any issues.
- Python: There are numerous E501: Line Too Long errors in Python files however shortening them inhibits code readability and therefore they have been ignored. Other that these warnings all pages are PEP8 compliant.

### Formatter
- HTML: [HTML Formatter](https://codebeautify.org/htmlviewer/) - Set the tab size to 4.
- CSS: [CSS Formatter](https://webformatter.com/css) - Set the tab size to 4.
- Python: [PEP8 online](http://pep8online.com/)

# Compatibility and Responsiveness
The device emulator by Google Chrome's developer tool was used to check the responsiveness across all  different screen sizes and devies to ensure compatibility and responsiveness. Also, this website has been tested on multiple browsers (Chrome, Safari and Edge. An iPhone 11 was used for mobile testing.