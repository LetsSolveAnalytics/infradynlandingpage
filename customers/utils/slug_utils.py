from django.utils.text import slugify
import random
import string


def generate_unique_slug(instance, title, slug_field_name='slug'):
    slug = slugify(title)
    model_class = instance.__class__
    unique_slug = slug

    # Check if the slug exists
    while model_class.objects.filter(**{slug_field_name: unique_slug}).exists():
        unique_slug = f"{slug}-{random.randint(1000,9999)}"

    return unique_slug
