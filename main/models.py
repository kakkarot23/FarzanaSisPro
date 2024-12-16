from django.db import models

# Create your models here.

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    dp = models.DecimalField(max_digits=10, decimal_places=2)
    wp = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    reorder_level = models.IntegerField()

    def __str__(self):
        return self.name




class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name



class Supplier(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name



class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Invoice {self.id} - {self.customer.name}"



