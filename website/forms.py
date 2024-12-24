from django import forms

from website.models import Page, GlobalSettings


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = '__all__'


class GlobalSettingsForm(forms.ModelForm):
    class Meta:
        model = GlobalSettings
        fields = '__all__'
