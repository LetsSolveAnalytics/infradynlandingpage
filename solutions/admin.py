from django.contrib import admin
from parler.admin import TranslatableAdmin

from .forms import SolutionForm


class SolutionAdmin(admin.ModelAdmin):
    form = SolutionForm

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status',)
    list_filter = ('status', )
