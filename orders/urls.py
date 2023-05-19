from django.urls import path, include
from .views import *

urlpatterns = [
    path('create/', order_create_view, name='checkout_create')
]
