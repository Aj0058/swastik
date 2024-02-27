from django.db import models
from django.contrib.auth.models import User

import datetime
import os

def get_file_path(instance, filename):
    original_filename = filename
    now_time = datetime.datetime.now().strftime('%y%m%d%H%M%S')
    filename ="%s%s" %(now_time,original_filename)
    return os.path.join('uploads/', filename)

class Category(models.Model):  
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="Whether the category is hidden or not")
    trending = models.BooleanField(default=False, help_text="Whether the category is trending or not")
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords = models.TextField(null=False, blank=False)
    meta_description = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    Product_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    Small_description = models.TextField(max_length=250, null=False, blank=False)
    Quantity = models.IntegerField(null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    Orignal_Price = models.FloatField(null=False, blank=False)
    Selling_Price =models.FloatField(null=False,blank=False)
    status = models.BooleanField(default=False, help_text="Whether the category is hidden or not")
    trending = models.BooleanField(default=False, help_text="Whether the category is trending or not")
    Tag = models.CharField(max_length=150, null=False, blank=False)
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords = models.TextField(null=False, blank=False)
    meta_description = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart - User: {self.user.username}, Product: {self.product.name}"

class Newproducts(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    Product_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    Small_description = models.TextField(max_length=250, null=False, blank=False)
    Quantity = models.IntegerField(null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    Orignal_Price = models.FloatField(null=False, blank=False)
    Selling_Price =models.FloatField(null=False,blank=False)
    status = models.BooleanField(default=False, help_text="Whether the category is hidden or not")
    trending = models.BooleanField(default=False, help_text="Whether the category is trending or not")
    Tag = models.CharField(max_length=150, null=False, blank=False)
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords = models.TextField(null=False, blank=False)
    meta_description = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
 