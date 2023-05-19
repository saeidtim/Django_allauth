from django.urls import path, include
from .views import *

# app_name = 'products'

urlpatterns = [
    path('all/', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='detail_view'),
]
