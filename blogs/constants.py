from django.db import models
from django.utils.translation import gettext_lazy as _


class PostType(models.IntegerChoices):
    BLOG = 0, _("Blog")
    CASESTUDY = 3, _("Casestudy")


class CommentStatus(models.IntegerChoices):
    PENDING = 0, _("Pending")
    APPROVED = 1, _("Approved")
    REJECTED = 2, _("Rejected")
