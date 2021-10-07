import datetime
from django.db.models.signals import pre_save, post_save
from django.db import models

from django.contrib.auth.models import AbstractUser
# from django.db.models.fields.related import OneToOneField

class User(AbstractUser):
    # mobile_nubmer = models.IntegerField(unique=True,max_length=)
    expiry_date=models.DateTimeField()
    # USERNAME_FIELD = "mobile_nubmer"
def pre_save_receiver(sender, instance, *args, **kwargs):
    now= datetime.datetime.now()+datetime.timedelta(minutes=3)
    instance.expiry_date=now
  
pre_save.connect(pre_save_receiver, sender = User)
post_save.connect(pre_save_receiver, sender = User)

class Customer(models.Model):
    customer_name = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    email_address = models.EmailField(max_length=255,unique=True)
    mobile_number = models.CharField(max_length=15)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField()
    def __str__(self):
        return self.customer_name
def pre_save_receiver_created_date(sender, instance, *args, **kwargs):
    now= datetime.datetime.now()
    instance.created_date=now
pre_save.connect(pre_save_receiver_created_date, sender = Customer)
post_save.connect(pre_save_receiver_created_date, sender = Customer)

class ImageUpload(models.Model):
    customer_id = models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)
    imagepath = models.ImageField(upload_to='profilePic',blank=True ,null=True)
    created_at = models.DateTimeField()
    status = models.BooleanField(default=False)
    def __str__(self):
        return "Customer Id" % self.id
def pre_save_receiver_created_date(sender, instance, *args, **kwargs):
    now= datetime.datetime.now()
    instance.created_at=now
pre_save.connect(pre_save_receiver_created_date, sender = ImageUpload)
post_save.connect(pre_save_receiver_created_date, sender = ImageUpload)



