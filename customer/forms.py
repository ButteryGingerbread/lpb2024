from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    CONDITION_CHOICES = [
        ('diabetes', 'Diabetes'),
        ('low-sodium', 'Low Sodium'),
        ('gluten-free', 'Gluten Free'),
        ('autism', 'Autism'),
    ]

    condition = forms.ChoiceField(choices=CONDITION_CHOICES, required=True)

    class Meta:
        model = Customer
        fields = ['name', 'condition']
