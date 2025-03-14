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

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'required': True}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'required': True}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject', 'required': True}),
            'message': forms.Textarea(attrs={'placeholder': 'Message', 'required': True}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = False

    def as_divs(self):
        """Custom form rendering with each field wrapped in a div."""
        return "\n".join(
            f'<div class="col-md-12 col-sm-12 col-lg-12">{field}</div>'
            for field in self
        )
