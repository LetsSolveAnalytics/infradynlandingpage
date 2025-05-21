from django.db import models
from django.utils.translation import gettext_lazy as _


class SolutionType(models.IntegerChoices):
    PROJECTFOCUS = 0, _("ProjectFocus")
    JOBROLE = 1, _("JobRole")
