from django.urls import path
from .views import (
    create_sku,
)

urlpatterns = [
    path('create/', create_sku, name='create_sku'),
]
