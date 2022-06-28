# from distutils.command.upload import upload
# from email.policy import default
# from pyexpat import model
# from xml.etree.ElementInclude import default_loader
import email
from unicodedata import name
from django.db import models
from django.forms import IntegerField

# from shopping.shop.views import product

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    Category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images",default="")
    
    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=300)
    phone = models.CharField(max_length=70,default="")
    desc = models.CharField(max_length=500,default="")
    
    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    amount = models.IntegerField(default=0)
    phone = models.CharField(max_length=111,default='')
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    pincode = models.CharField(max_length=111)

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7]+"..."
    
