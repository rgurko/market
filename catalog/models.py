from django.db import models


class Category(models.Model):
    name = models.CharField('Category name', max_length=50, null=False)
    slug = models.SlugField(max_length=50, null=False)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(verbose_name='Product name', max_length=200, blank=False, null=False)
    description = models.TextField('Description', blank=True, null=True)
    price = models.DecimalField('Price', max_digits=10, decimal_places=2, null=False)
    discount = models.IntegerField('Discount', help_text="in percents", default=0)
    picture = models.ImageField('Picture', upload_to="products/%Y/%m/%d", blank=True, default="default.png")
    stock = models.PositiveIntegerField('Stock', default=0)
    is_available = models.BooleanField('Available', default=False)
    slug = models.SlugField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        indexes = [models.Index(fields=['slug'])]

    def __str__(self):
        return f"{self.name} - {self.price}"


