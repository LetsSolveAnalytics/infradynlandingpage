from django.db import models
from django.utils.functional import cached_property
from parler.models import TranslatedFields

from .constants import PostType, CommentStatus
from .utils import slug_utils
from coreapp.base import BaseModel, BaseTranslateModel


# Create your models here.

class Category(BaseTranslateModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=100)
    )
    slug = models.SlugField(unique=True, db_index=True, editable=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}"

    def save(self, *args, **kwargs):
        name = self.safe_translation_getter("name")
        if name and not self.slug:
            self.slug = slug_utils.generate_unique_slug(self, name)
        super().save(*args, **kwargs)


class Post(BaseTranslateModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=100),
        content=models.TextField(null=True, blank=True)
    )
    image = models.ImageField(upload_to='blog/images/', default='default.png')
    slug = models.SlugField(unique=True, db_index=True, editable=False)
    date_time = models.DateTimeField(null=True, blank=True)
    post_type = models.SmallIntegerField(choices=PostType.choices)
    is_published = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category)

    @cached_property
    def get_comments(self):
        return self.comment_set.all()

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
    status = models.SmallIntegerField(choices=CommentStatus.choices, default=CommentStatus.PENDING)

    def __str__(self):
        return f"{self.name}: {self.subject} - {self.status}"
