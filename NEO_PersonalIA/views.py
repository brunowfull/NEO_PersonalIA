from django.shortcuts import render, redirect
from .models import User, Product, Order
from .forms import ProductForm, OrderForm

# View for displaying and adding products

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

# View for displaying products

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

# View for creating an order

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_summary')
    else:
        form = OrderForm()
    return render(request, 'create_order.html', {'form': form})
