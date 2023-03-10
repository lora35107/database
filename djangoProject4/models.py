from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)
    email = models.EmailField(max_length=50, blank=True, null=False)
    age = models.IntegerField(max_length=50, blank=True, null=False)
    country = models.CharField(max_length=50,  blank=True, null=False)
    amount = models.CharField(max_length=50,  blank=True, null=False)
    gender = models.CharField(max_length=50, blank=True, null=False)
    phone = models.IntegerField(max_length=50, default=3, blank=True, null=False)

class Product(models.Model):
    productname = models.CharField(max_length=50, blank=True, null=False)
    productprice = models.CharField(max_length=50, blank=True, null=False)
    productdescription = models.CharField(max_length=50, blank=True, null=False)
    productquantity = models.CharField(max_length=50, blank=True, null=False)

def __str__(self):
    return self.name
