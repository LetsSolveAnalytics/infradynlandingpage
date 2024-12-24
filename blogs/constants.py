from django.db import models
from django.utils.translation import gettext_lazy as _


class PostType(models.IntegerChoices):
    BLOG = 0, _("Blog")
    NEWS = 1, _("News")
    EVENT = 2, _("Event")
