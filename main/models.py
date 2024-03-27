from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    
    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
    

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10) # +
    discount_price = models.DecimalField(decimal_places=2, max_digits=10, 
                                         blank=True, null=True) #+
    banner_img = models.ImageField(upload_to='banner-img')
    quantity = models.IntegerField() 
    delivery = models.BooleanField(default=False) #+


class ProductImg(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='img')


class ProductVideo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    video = models.FileField(upload_to='video')
    link = models.URLField(null=True, blank=True)


class Review(models.Model):
    mark = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()