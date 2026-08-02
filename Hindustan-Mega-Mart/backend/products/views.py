from django.shortcuts import render
from .models import Product, Category

def home(request):

    # Read search text from URL
    search_query = request.GET.get("search", "")

    # Get all active categories
    categories = Category.objects.filter(is_active=True)

    # Filter products if search text exists
    if search_query:
        products = Product.objects.filter(
            name__icontains=search_query,
            is_active=True
        )
    else:
        products = Product.objects.filter(is_active=True)

    context = {
        "products": products,
        "categories": categories,
        "search_query": search_query,
    }

    return render(request, "products/home.html", context)