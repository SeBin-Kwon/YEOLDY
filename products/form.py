from django import forms
from .models import Products


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            "name",
            "cost",
            "cost_2",
            "category",
            "color",
            "size",
            "sale_percent",
        ]
