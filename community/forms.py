from django import forms
from .models import QnA, Review, Photo


class QnaForm(forms.ModelForm):
    class Meta:
        model = QnA
        fields = [
            "title",
            "content",
            "image",
            "solve",
            "password",
        ]
        widgets = {"password": forms.PasswordInput()}


class UpdateQnaForm(QnaForm):
    class Meta:
        model = QnA
        fields = [
            "title",
            "content",
            "image",
        ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "title",
            "content",
            "grade",
        ]
