from django.shortcuts import render
from .models import Product, Category

def home(request):

    search_query = request.GET.get("search", "")
    category_slug = request.GET.get("category", "")

    categories = Category.objects.filter(is_active=True)

    products = Product.objects.filter(is_active=True)

    # Search Filter
    if search_query:
        products = products.filter(
            name__icontains=search_query
        )

    # Category Filter
    if category_slug:
        products = products.filter(
            category__slug=category_slug
        )

    context = {
        "products": products,
        "categories": categories,
        "search_query": search_query,
        "selected_category": category_slug,
    }

    return render(request, "products/home.html", context)