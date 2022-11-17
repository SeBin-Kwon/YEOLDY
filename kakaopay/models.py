from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

order_requests = (
    ("부재 시 경비실에 맡겨주세요", "부재 시 경비실에 맡겨주세요"),
    ("부재 시 택배함에 넣어주세요", "부재 시 택배함에 넣어주세요"),
    ("부재 시 집 앞에 놔주세요", "부재 시 집 앞에 놔주세요"),
    ("배송 전 연락 바랍니다", "배송 전 연락 바랍니다"),
    ("파손의 위험이 있는 상품입니다. 배송 시 주의해 주세요.", "파손의 위험이 있는 상품입니다. 배송 시 주의해 주세요."),
)

class OrderList(models.Model):
    location_name = models.CharField(max_length=20)
    order_name = models.CharField(max_length=20)
    location = models.TextField()
    phone_number = PhoneNumberField(unique=True, null=True, blank=True, region="KR")
    order_request = models.CharField(max_length=50, choices=order_requests)