from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=100, unique=True)

    slug = models.SlugField(max_length=100, unique=True)

    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Brand(models.Model):

    name = models.CharField(max_length=100, unique=True)

    slug = models.SlugField(max_length=100, unique=True)

    logo = models.ImageField(
        upload_to="brands/",
        null=True,
        blank=True
    )

    description = models.TextField(blank=True)

    website = models.URLField(
        blank=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name    

    
class Product(models.Model):
    category = models.ForeignKey(
    Category,
    on_delete=models.CASCADE,
    related_name="products",
    null=True,
    blank=True
)
    brand = models.ForeignKey(
    Brand,
    on_delete=models.CASCADE,
    related_name="products",
    null=True,
    blank=True
)
    
    image = models.ImageField(
    upload_to="products/",
    null=True,
    blank=True
)
    name = models.CharField(max_length=200)

    slug = models.SlugField(max_length=200, unique=True)

    description = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    stock = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField(
        upload_to="products/gallery/"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} Image"
