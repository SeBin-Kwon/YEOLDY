from django import forms
from .models import Style, Style_Review


class StyleForm(forms.ModelForm):
    class Meta:
        model = Style
        fields = [
            "title",
            "content",
            "tag",
        ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Style_Review
        fields = [
            "content",
        ]
