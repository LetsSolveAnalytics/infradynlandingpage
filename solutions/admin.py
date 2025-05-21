from django.contrib import admin
from parler.admin import TranslatableAdmin


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status',)
    list_filter = ('status', )
