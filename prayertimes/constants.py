from django.db import models
from django.utils.translation import gettext_lazy as _


class PrayerType(models.IntegerChoices):
    FAJR = 0, _("Fajr")
    DHUHR = 1, _("Dhuhr")
    ASR = 2, _("Asr")
    MAGHRIB = 3, _("Maghrib")
    ISHA = 4, _("Isha")
