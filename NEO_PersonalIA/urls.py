from django.contrib import admin
from django.urls import path
from .views import add_product, product_list, create_order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-product/', add_product, name='add_product'),
    path('products/', product_list, name='product_list'),
    path('create-order/', create_order, name='create_order'),
]