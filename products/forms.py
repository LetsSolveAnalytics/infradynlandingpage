# forms.py
from django import forms
from .models import Product, ProductFeature

class ProductForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=ProductFeature.objects.filter(is_active=True),
        widget=forms.CheckboxSelectMultiple,  # or use forms.SelectMultiple
        required=True
    )

    class Meta:
        model = Product
        fields = '__all__'
