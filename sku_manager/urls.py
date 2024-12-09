from django.urls import path
from .views import (
    read_skus
    create_sku,
)

urlpatterns = [
    path('read/', read_skus, name='read_skus'),
    path('create/', create_sku, name='create_sku'),
]
