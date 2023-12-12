from django.db import models
from mydjangodevops.common.models import BaseModel

class Product(BaseModel):
    name = models.TextField()




