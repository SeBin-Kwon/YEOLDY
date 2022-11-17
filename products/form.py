from django import forms
from .models import Products


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            "name",
            "cost",
            "category",
            "color",
            "size",
            "image",
            "new_product",
        ]
