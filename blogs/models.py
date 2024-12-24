from django.db import models
from parler.models import TranslatedFields

from .constants import PostType
from .utils import slug_utils
from coreapp.base import BaseModel


# Create your models here.

class Post(BaseModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=100),
        content=models.TextField(null=True, blank=True)
    )
    image = models.ImageField(upload_to='blog/images/', default='default.png')
    slug = models.SlugField(unique=True, db_index=True, editable=False)
    date_time = models.DateTimeField(null=True, blank=True)
    post_type = models.SmallIntegerField(choices=PostType.choices)
    is_published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        title = self.safe_translation_getter("title")
        if title and not self.slug:
            self.slug = slug_utils.generate_unique_slug(self, title)
        super().save(*args, **kwargs)


class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    desc = models.CharField(max_length=600)
