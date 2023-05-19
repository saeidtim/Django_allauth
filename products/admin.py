from django.contrib import admin
from .models import *


class CommentProductAdmin(admin.TabularInline):
    model = ProductComment
    fields = ['author', 'body', 'stars', ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active', ]
    inlines = [
        CommentProductAdmin,
    ]

