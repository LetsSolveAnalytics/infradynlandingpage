from django.apps import apps
from django.contrib import admin
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _
from parler.admin import TranslatableAdmin
from parler.models import TranslatableModel

from blogs.admin import CommentAdmin
from blogs.models import Post, Comment
from coreapp.models import User


# Custom admin for User to ensure password hashing
class CustomUserAdmin(admin.ModelAdmin):
    ordering = ["email"]
    list_display = ["email", "first_name", "last_name", "is_staff"]

    def save_model(self, request, obj, form, change):
        if form.cleaned_data.get("password") and not obj.password.startswith("pbkdf2_"):
            obj.password = make_password(form.cleaned_data["password"])
        super().save_model(request, obj, form, change)


class CustomPostAdmin(TranslatableAdmin):
    list_display = ("get_title", "post_type")
    list_filter = ("post_type", "is_published")

    def get_title(self, obj):
        return obj.safe_translation_getter("title", any_language=True)

    get_title.short_description = _("Title")


models = apps.get_models()

for model in models:
    if not admin.site.is_registered(model):
        if isinstance(model, type) and issubclass(model, TranslatableModel):
            if model == Post:
                admin.site.register(Post, CustomPostAdmin)
            else:
                admin.site.register(model, TranslatableAdmin)
        elif isinstance(model, type) and issubclass(model, Comment):
            admin.site.register(Comment, CommentAdmin)
        elif isinstance(model, type) and issubclass(model, User):
            admin.site.register(User, CustomUserAdmin)
        else:
            admin.site.register(model)

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'designation')

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('question', 'answer')
