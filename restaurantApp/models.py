
from django.db import models
from datetime import datetime
from django.conf import settings
import uuid
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class User(AbstractUser):
    customer = models.BooleanField(default = False)
    staff = models.BooleanField(default = False)
    administrative = models.BooleanField(default = False)

    
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank =True, on_delete=models.CASCADE)
    surname = models.CharField(max_length=100, null= True)
    midname = models.CharField(max_length=100, null= True)
    first_name = models.CharField(max_length=100, null= True)
    about = models.CharField(max_length=100, null= True)
    gender = models.CharField(max_length=100, null=True)
    whatsapp_Number = models.IntegerField(unique=True, null= True)
    phone_number = models.IntegerField()
    profile_image = models.ImageField(upload_to='static/profile_images', null=True, blank=True)


    def __str__(self):
        return str(self.surname)

    @property
    def profileURL(self):
        try:
            url = self.profile_image.url
        except:
            url=''
        return url


class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=True)
    details = models.CharField(max_length=200)
    menu_image = models.ImageField(upload_to='static/images', null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.menu_image.url
        except:
            url=''
        return url


class OrderItem(models.Model):
    item = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(null=True)
    

    def __str__(self):
        return str(self.item)

    @property
    def unit_total(self):
        unit_total = self.item.price * self.quantity
            
        return unit_total



    

    



class Reciept(models.Model):
    customer = models.OneToOneField(User, null=True, blank =True, on_delete=models.CASCADE)
    order = models.CharField(max_length=2000,null= True)
    Total = models.FloatField(null=True)
    phone_contact = models.IntegerField(null=True)
    destination = models.CharField(max_length=100, null= True)
    transaction_id = models.UUIDField(default=uuid.uuid4)
    date_Ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default= False)

    def __str__(self):
        return str(self.date_Ordered)



    
   

    
    

