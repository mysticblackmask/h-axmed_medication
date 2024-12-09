from django.urls import path
from .views import (
    read_skus
    create_sku,
    update_sku,
)

urlpatterns = [
    path('read/', read_skus, name='read_skus'),
    path('create/', create_sku, name='create_sku'),
    path('update/<int:pk>/', update_sku, name='update_sku'),
]
