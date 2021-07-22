# Register your models here.
from django.contrib import admin
from .models.product import Product



class AdminProduct(admin.ModelAdmin):
    list_display = ['name','weight','created_at','updated_at']

admin.site.register(Product, AdminProduct)
