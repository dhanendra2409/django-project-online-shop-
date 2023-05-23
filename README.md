# django-project-online-shop-
A Simple single vendor Online shoppping project basically a part of my learning.I have also used djangorestframework to get and post product Information (just to show a basic use of Django Rest Framework to create an api).

## FUNCTIONALITIES
### Customer
* Customer can view/search products without login.
* Customer can also add/remove product to cart without login (if customer try to add same product in cart. It will add only one)
* When customer try to purchase product, then he/she must login to system.
* After creating account and login to system, he/she can place order.
* There is a payment page is just for demo.
* If customer click on pay button, then their payment will be successful and their order will be placed.
* Customer can check their ordered details by clicking on orders button.
* Customer can see the order status (Pending, Confirmed, Delivered) for each order
* Customer can Download their order invoice for each order
* Customer can send feedback to admin (without login)
* Customer can hae a look on use of **API by clicking API Products** on Navbar

### Admin
* First admin will login ( for username/password run following command in cmd )
``` 
py manage.py createsuperuser
```
* Give username, email, password and your admin account will be created.
* After login, there is a dashboard where admin can see how many customer is registered, how many products are   there for sale, how many orders placed.
* Admin can add/delete/view/edit the products.
* Admin can view/edit/delete customer details.
* Admin can view/delete orders.
* Admin can change status of order (order is pending, confirmed, out for delivery, delivered)
* Admin can view the feedbacks sent by customers.

### Some Important Features
* customer places order and admin deleted that user(fraud detection), then their orders will automatically deleted
* suppose 1 customer places 4 products order and admin deleted 2 product from website, then that 2 product order will also be deleted and   other 2 will be their
* If user click on purchase button without having products in their cart, then website will ask to add product in cart first.
* Same Login page for Customer and Admin,so just by entering credentials they will be redirected to their respective dashboard.
* Admin can be created onlyfrom cmd by creating superuser. 

## HOW TO RUN THIS PROJECT
* Download This Project Zip Folder and Extract it
* Move to project folder in Terminal. Then run following Commands :
``` 
python -m venv <your venv name>
<your venv name>\Scripts\activate
pip install -r requirement.txt 
```
``` 
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
#### Note:- Python(latest) must be installed
* Now enter following URL in Your Browser Installed On Your Pc
http://127.0.0.1:8000/

##### If you are getting error like
```
ImportError: urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with LibreSSL 2.8.3. See: https://github.com/urllib3/urllib3/issues/2168
``` 
* just install this below and problem will be sorted then do migrations.
```
python3 -m pip install urllib3==1.26.6
```
* After this create superuser and add or manage products and customers.

## How to use API 
* The api here is a Self Describing API ,The documentation for each API endpoint can be provided simply by visiting the URL in your browser.
* You can hover over Product view in Navbar and choose either to post products info or to get the posted ones.
* To Post product info we need to go to post product option and enter data in json format ,
* you can also visit
```
http://127.0.0.1:8000/postproduct/
```
* and add product info under following headings,
```
{
        "name": "iphone",
        "description": "an apple product",
        "total_buyers": 15
    }
```
* After this you can go to Get Product Option or just type this below in browser and you can access the data
```
http://127.0.0.1:8000/getproduct/
```


## Some Drawbacks and issues
* There are some more work needed in contact us form.
* As it is an ongoing project so there may be some issue arrises,they might be:-
   * When user edit their profile then he/she must login again because their username/password is updated in db.
   * Popup of product is added to cart is shown when click on Ecommerce logo (soon will be fixed)

### This Project is been created for learning purpose and i have created this by learning from various tutorials and videos.
### There may be some functionalities not working properly so this must not be used for real application.
