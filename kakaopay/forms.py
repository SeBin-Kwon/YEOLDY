from django import forms
from .models import OrderList


class OrderlistForm(forms.ModelForm):
    class Meta:
        model = OrderList
        fields = [
            "location_name",
            "order_name",
            "phone_number",
            "order_request"
        ]
        labels = {
            "location_name": "배송지명",
            "order_name": "주문자",
            "phone_number": "연락처",
            "order_request": "배송시 요청사항"
        }