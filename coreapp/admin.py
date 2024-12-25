from django.contrib import admin
from django.apps import apps
from parler.admin import TranslatableAdmin
from parler.models import TranslatableModel

from prayertimes.admin import PrayerTimeAdmin
from prayertimes.models import PrayerTime

models = apps.get_models()

for model in models:
    if not admin.site.is_registered(model):
        if isinstance(model, type) and issubclass(model, TranslatableModel):
            admin.site.register(model, TranslatableAdmin)
        elif isinstance(model, type) and issubclass(model, PrayerTime):
            admin.site.register(PrayerTime, PrayerTimeAdmin)
        else:
            admin.site.register(model)



