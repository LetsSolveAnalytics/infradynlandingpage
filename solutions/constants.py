from django.db import models
from django.utils.translation import gettext_lazy as _


class SolutionType(models.IntegerChoices):
    PROJECT = 0, _("Project")
    ROLE = 1, _("Role")
    FIRM = 2, _("Firm")

