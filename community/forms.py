from django import forms
from .models import QnA, Review
from .widgets import starWidget


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
            "image",
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
        widgets = {"grade": starWidget}
        labels = {"title": "제목", "content": "본문", "grade": "평점"}
