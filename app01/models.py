from django.db import models

# Create your models here.

class Customers(models.Model):
    name = models.CharField(max_length=255)
    family = models.CharField(max_length=255)
    birth_year = models.IntegerField()
    ssn = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    class Meta:
        db_table = "customers"
class Brand(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        db_table="brands"
class Category(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        db_table="categories"
class Product(models.Model):
    name =models.CharField(max_length=255)
    price = models.IntegerField()
    brand = models.ForeignKey(Brand,on_delete=models.DO_NOTHING)
    categories = models.ManyToManyField(Category)
    class Meta:
        db_table = "products"
class Seller(models.Model):
    name = models.CharField(max_length=255)
    address =  models.CharField(max_length=255)
    class Meta:
        db_table="sellers"