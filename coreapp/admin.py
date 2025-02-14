from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.hashers import make_password
from django.apps import apps
from parler.admin import TranslatableAdmin
from parler.models import TranslatableModel

from blogs.admin import CommentAdmin
from blogs.models import Post, Comment
from prayertimes.admin import PrayerTimeAdmin
from prayertimes.models import PrayerTime
from coreapp.models import User

# Custom admin for User to ensure password hashing
class CustomUserAdmin(UserAdmin):
    def save_model(self, request, obj, form, change):
        if form.cleaned_data.get("password") and not obj.password.startswith("pbkdf2_"):
            obj.password = make_password(form.cleaned_data["password"])
        super().save_model(request, obj, form, change)

models = apps.get_models()

for model in models:
    if not admin.site.is_registered(model):
        if isinstance(model, type) and issubclass(model, TranslatableModel):
            admin.site.register(model, TranslatableAdmin)
        elif isinstance(model, type) and issubclass(model, PrayerTime):
            admin.site.register(PrayerTime, PrayerTimeAdmin)
        elif isinstance(model, type) and issubclass(model, Comment):
            admin.site.register(Comment, CommentAdmin)
        elif isinstance(model, type) and issubclass(model, User):
            admin.site.register(User, CustomUserAdmin)
        else:
            admin.site.register(model)
