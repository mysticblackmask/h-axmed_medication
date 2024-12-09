from django.urls import path
from .views import (
    read_skus
    create_sku,
    update_sku,
    delete_sku,
    bulk_create_skus
)

urlpatterns = [
    path('read/', read_skus, name='read_skus'),
    path('create/', create_sku, name='create_sku'),
    path('update/<int:pk>/', update_sku, name='update_sku'),
    path('delete/<int:pk>/', delete_sku, name='delete_sku'),
    path('bulk-create/', bulk_create_skus, name='bulk_create_skus'),
]
