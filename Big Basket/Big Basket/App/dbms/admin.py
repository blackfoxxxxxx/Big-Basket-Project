from django.contrib import admin
from .models import*

@admin.register(Products)
class ModelAdmin(admin.ModelAdmin):
    list_display=["id","product_name","date_of_mnf","date_of_exp"]


@admin.register(Customer)
class ModelAdmin(admin.ModelAdmin):
    list_display=["id","customer_name","phone_number","address"]


@admin.register(Orders)
class ModelAdmin(admin.ModelAdmin):
    list_display=["id","order_name","order_date"]


@admin.register(Payment)
class ModelAdmin(admin.ModelAdmin):
    list_display=["id","Payment_mode","amount"]


@admin.register(Order_details)
class ModelAdmin(admin.ModelAdmin):
    list_display=["id","order_quantity"]

    