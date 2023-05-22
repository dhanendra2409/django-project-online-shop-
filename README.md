# django-project-online-shop-
A Simple Online shoppping project basically a part of my learning.I have also used djangorestframework to get and post product Information (just to show a basic use of Django Rest Framework to create an api).

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

## HOW TO RUN THIS PROJECT
* Install Python(3.7.6) (Dont Forget to Tick Add to Path while installing Python)
* Open Terminal and Execute Following Commands :
``` 
pip install -r requirement.txt 
```

* Download This Project Zip Folder and Extract it
* Move to project folder in Terminal. Then run following Commands :
``` 
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
* Now enter following URL in Your Browser Installed On Your Pc
http://127.0.0.1:8000/

## Some Drawbacks and issues
* There are some more work needed in contact us form.
* As it is an ongoing project so there may be some issue arrises,they might be:-
   * When user edit their profile then he/she must login again because their username/password is updated in db.
   * Popup of product is added to cart is shown when click on Ecommerce logo (soon will be fixed)

## In case if the css not loading properly 
* Run
``` 
pip install collectstatic
```
* but their must exist STATIC_ROOT in settings.py

### This Project is been created for learning purpose and i have created this by learning from various tutorials and videos.
### There may be some functionalities may not working properly so this must not be used for real application.
