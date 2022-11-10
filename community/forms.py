from django import forms
from .models import QnA,Review

class QnaForm(forms.ModelForm):
    class Meta:
        model = QnA
        fields =[
            'title',
            'content',
            'image',
            'solve',
        ]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields =[
            'title',
            'content',
            'image',
            'grade',
        ]