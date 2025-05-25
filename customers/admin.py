from django.contrib import admin
from parler.admin import TranslatableAdmin

from .forms import CustomerForm


class CustomerAdmin(admin.ModelAdmin):
    form = CustomerForm

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status',)
    list_filter = ('status', )
