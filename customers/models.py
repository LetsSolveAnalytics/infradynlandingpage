from django.db import models
from parler.models import TranslatedFields

from .utils import slug_utils
from coreapp.base import BaseModel, BaseTranslateModel
from .constants import CustomerType


# Create your models here.

class CustomerFeature(BaseTranslateModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=100),
        description = models.TextField(null=True, blank=True)
    )
    slug = models.SlugField(unique=True, db_index=True, editable=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}"

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            name = self.safe_translation_getter("name")
            if name and not self.slug:
                self.slug = slug_utils.generate_unique_slug(self, name)
            super().save(*args, **kwargs)

class CustomerProductCategory(BaseModel):
    category_name = models.CharField(max_length=300)
    headline_title = models.CharField(max_length=300)
    # slug = models.SlugField(unique=True, db_index=True, editable=False)
    image = models.ImageField(upload_to='customer/images/', default='default.png')
    content = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

class Customer(BaseTranslateModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=100),
        content=models.TextField(null=True, blank=True),
    )
    image = models.ImageField(upload_to='customer/images/', default='default.png')
    slug = models.SlugField(unique=True, db_index=True, editable=False)
    # customer_type = models.SmallIntegerField(choices=CustomerType.choices)
    date_time = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    features = models.ManyToManyField(CustomerFeature)
    customer_product_category = models.ManyToManyField(CustomerProductCategory)

    def save(self, *args, **kwargs):
        title = self.safe_translation_getter("title")
        if title and not self.slug:
            self.slug = slug_utils.generate_unique_slug(self, title)
        super().save(*args, **kwargs)