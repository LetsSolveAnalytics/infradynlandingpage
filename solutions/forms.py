# forms.py
from django import forms
from .models import Solution, SolutionCategory

class SolutionForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=SolutionCategory.objects.filter(is_active=True),
        widget=forms.CheckboxSelectMultiple,  # or use forms.SelectMultiple
        required=True
    )

    class Meta:
        model = Solution
        fields = '__all__'
