from django import forms
from .models import QnA, Review, QnA_Review
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


class Qna_ReviewForm(forms.ModelForm):
    class Meta:
        model = QnA_Review
        fields = [
            "content",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].widget.attrs = {
            "placeholder": "댓글을 작성해 주세요",
        }
        self.fields["content"].help_text = None
