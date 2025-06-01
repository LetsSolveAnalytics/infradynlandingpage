from django.db import models
from parler.models import TranslatedFields

from .utils import slug_utils
from coreapp.base import BaseModel, BaseTranslateModel
from .constants import ProductType


# Create your models here.

class ProductFeature(BaseTranslateModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=100),
        description = models.TextField(null=True, blank=True)
    )
    image = models.ImageField(upload_to='product/images/', default='default.png')
    slug = models.SlugField(max_length=250, unique=True, db_index=True, editable=False)
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

class ProductUsage(BaseModel):
    name = models.CharField(max_length=300)
    content = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(BaseTranslateModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=100),
        content=models.TextField(null=True, blank=True),
        banner_title=models.CharField(max_length=250),
    )
    image = models.ImageField(upload_to='product/images/', default='default.png')
    slug = models.SlugField(max_length=250, unique=True, db_index=True, editable=False)
    product_type = models.SmallIntegerField(choices=ProductType.choices)
    date_time = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    features = models.ManyToManyField(ProductFeature)
    usages = models.ManyToManyField(ProductUsage)

    def save(self, *args, **kwargs):
        banner_title = self.safe_translation_getter("banner_title")
        if banner_title and not self.slug:
            self.slug = slug_utils.generate_unique_slug(self, banner_title)
        super().save(*args, **kwargs)