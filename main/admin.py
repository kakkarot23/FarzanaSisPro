from django.contrib import admin
from .models import Product, Customer, Supplier, Invoice

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Invoice)
