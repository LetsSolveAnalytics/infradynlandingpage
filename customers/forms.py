# forms.py
from django import forms
from .models import Customer, CustomerFeature

class CustomerForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=CustomerFeature.objects.filter(is_active=True),
        widget=forms.CheckboxSelectMultiple,  # or use forms.SelectMultiple
        required=True
    )

    class Meta:
        model = Customer
        fields = '__all__'
