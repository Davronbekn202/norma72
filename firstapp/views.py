from django.shortcuts import render, get_object_or_404
from .models import Category


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})


def category_products(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = category.products.all()

    return render(request, 'category_products.html', {
        'category': category,
        'products': products
    })