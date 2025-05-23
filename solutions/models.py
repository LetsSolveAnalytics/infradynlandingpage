from django.db import models
from parler.models import TranslatedFields

from .constants import SolutionType
from .utils import slug_utils
from coreapp.base import BaseModel, BaseTranslateModel


# Create your models here.

class SolutionCategory(BaseTranslateModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=100),
        description = models.TextField(null=True, blank=True)
    )
    image = models.ImageField(upload_to='solution/images/', default='default.png')
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


class Solution(BaseTranslateModel):
    translations = TranslatedFields(
        banner_title=models.CharField(max_length=100),
        banner_content=models.TextField(null=True, blank=True),
        secondary_title=models.CharField(max_length=200),
        introduction=models.TextField(null=True, blank=True)
    )
    image = models.ImageField(upload_to='solution/images/', default='default.png')
    slug = models.SlugField(unique=True, db_index=True, editable=False)
    date_time = models.DateTimeField(null=True, blank=True)
    solution_type = models.SmallIntegerField(choices=SolutionType.choices)
    is_published = models.BooleanField(default=False)
    categories = models.ManyToManyField(SolutionCategory)

    def save(self, *args, **kwargs):
        banner_title = self.safe_translation_getter("banner_title")
        if banner_title and not self.slug:
            self.slug = slug_utils.generate_unique_slug(self, banner_title)
        super().save(*args, **kwargs)