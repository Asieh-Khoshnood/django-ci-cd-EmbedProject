from django.db.models import QuerySet
from mydjangodevops.blog.models import Product


def get_products() -> QuerySet[Product]:
        return Product.objects.all()
