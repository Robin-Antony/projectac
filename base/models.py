from email.policy import default
from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser
from. manager import UserManager
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = None
    first_name = models.CharField(max_length=200,null=True,blank=True)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    phone = models.CharField(max_length=15,null=True)
    avatar = models.ImageField(verbose_name='Profile Pic',null=True,blank=True, default='avathar.svg')
    documents = models.FileField(verbose_name='upload your certificates(PDF) ',null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


    @property
    def imageURL(self):
        try:
            url = self.avatar.url
        except:
            url =''
        return url


class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length =12)
    address = models.TextField(verbose_name='address',max_length=500,blank=True,null=True)
    problem = models.TextField(verbose_name='How Can We Help You?(optional) ',max_length=700,blank=True,null=True)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now=True)
    order_no = models.IntegerField(default=0)
    accured_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)# staff ultered
    accured = models.BooleanField(default=False)
    order_price = models.FloatField(default=0,blank=True,null=True)
    history = models.TextField(max_length=1000,default='',blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


RATE_CHOICES = [
    (1, '1- Very Bad'),
    (2, '1- Bad'),
    (3, '1- Ok'),
    (4, '1- Good'),
    (5, '1- Very Good'),
]

class Rating(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True)# staff ultered
    rated = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    body = models.TextField(max_length=1000,blank=True,null=True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.order.name


class AccurOrder(models.Model):
    staff = models.ForeignKey(User,on_delete=models.CASCADE,null=True)# staff ultered
    order = models.OneToOneField(Order,on_delete=models.SET_NULL,null=True)
    complete = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

class Feedback(models.Model):
    name = models.CharField(max_length=200)
    feedback = models.TextField(max_length=800,default='')
    suggestion = models.TextField(max_length=800, default='')
    created = models.DateTimeField(auto_now_add = True)


class QandA(models.Model):
    name = models.CharField(max_length=200)
    question = models.TextField(max_length=300)
    answer = models.TextField(max_length=500,default="",blank=True)
    answered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add = True)
