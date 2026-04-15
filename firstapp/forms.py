from django import forms
from .models import Product

Product.objects.create(
    name="Iphone 15",
    description="New smartphone",
    price=1200,
    quantity=5
)

Product.objects.create(
    name="Samsung S24",
    description="Android flagship",
    price=1000,
    quantity=8
)

Product.objects.create(
    name="Laptop HP",
    description="Powerful laptop",
    price=1500,
    quantity=3
)
