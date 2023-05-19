from django.contrib import admin
from .models import *


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ['user', 'is_paid', ]


@admin.register(OrderItem)
class AdminOrder(admin.ModelAdmin):
    list_display = ['order', 'product', ]
