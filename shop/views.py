from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from cart.forms import CartAddProductForm
from shop.models import Category, Product



def base_view(request):
	categories = Category.objects.all()
	products = Product.objects.all()
	context = {
		'categories': categories,
		'products': products
	}
	return render(request, 'base.html', context)


def product_view(request, product_slug):
	product = Product.objects.get(slug=product_slug)
	cart_product_form = CartAddProductForm()
	context = {
		'product': product,
		'cart_product_form': cart_product_form
	}
	return render(request, 'product.html', context)


def category_view(request, category_slug):
	category = Category.objects.get(slug=category_slug)
	context = {
		'category': category
	}
	return render(request, 'category.html', context)