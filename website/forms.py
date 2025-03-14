from captcha.fields import CaptchaField
from django import forms

from website.models import Page, GlobalSettings, ContactMessage


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = '__all__'


class GlobalSettingsForm(forms.ModelForm):
    class Meta:
        model = GlobalSettings
        fields = '__all__'


class ContactMessageForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = ContactMessage
        fields = ('name', 'phone', 'email', 'subject', 'message')
