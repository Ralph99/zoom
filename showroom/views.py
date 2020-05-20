from django.shortcuts import render, get_object_or_404
from .models import Category, Product

from django.core.paginator import Paginator


# Create your views here.

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    #pagination

    paginator = Paginator(products, 9)

    page = request.GET.get('page')

    products = paginator.get_page(page)
    #pagination ends

    return render(request, 'showroom/product_list.html', {'category': category, 'categories': categories, 'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    return render(request, 'showroom/product_details.html', {'product': product,})
