from django.shortcuts import render
from .models import Product, Category, Brand


def home(request):

    search_query = request.GET.get("search", "")
    category_slug = request.GET.get("category", "")
    brand_slug = request.GET.get("brand", "")

    min_price = request.GET.get("min_price", "")
    max_price = request.GET.get("max_price", "")

    categories = Category.objects.filter(is_active=True)
    brands = Brand.objects.filter(is_active=True)
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

    # Brand Filter
    if brand_slug:
        products = products.filter(
            brand__slug=brand_slug
        )

    # Minimum Price Filter
    if min_price:
        products = products.filter(
            price__gte=min_price
        )

    # Maximum Price Filter
    if max_price:
        products = products.filter(
            price__lte=max_price
        )

    context = {
        "products": products,
        "categories": categories,
        "brands": brands,
        "search_query": search_query,
        "selected_category": category_slug,
        "selected_brand": brand_slug,
        "min_price": min_price,
        "max_price": max_price,
    }

    return render(request, "products/home.html", context)