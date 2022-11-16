from django import forms
from .models import QnA, Review


class QnaForm(forms.ModelForm):
    class Meta:
        model = QnA
        fields = [
            "title",
            "content",
            "image",
            "password",
        ]
        widgets = {"password": forms.PasswordInput()}


class QnaForm_2(forms.ModelForm):
    class Meta:
        model = QnA
        fields = [
            "title",
            "content",
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
