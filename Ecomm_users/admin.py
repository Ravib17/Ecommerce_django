from django.contrib import admin

from .models import Customer,Category,Product,Supplier,Order

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Order)
admin.site.register(Product)

# Register your models here.
