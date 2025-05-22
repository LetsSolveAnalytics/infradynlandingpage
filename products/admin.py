from django.contrib import admin
from parler.admin import TranslatableAdmin

from .forms import ProductForm


class ProductAdmin(admin.ModelAdmin):
    form = ProductForm

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status',)
    list_filter = ('status', )
