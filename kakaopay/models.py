from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model
from products.models import Products

order_requests = (
    ("부재 시 경비실에 맡겨주세요", "부재 시 경비실에 맡겨주세요"),
    ("부재 시 택배함에 넣어주세요", "부재 시 택배함에 넣어주세요"),
    ("부재 시 집 앞에 놔주세요", "부재 시 집 앞에 놔주세요"),
    ("배송 전 연락 바랍니다", "배송 전 연락 바랍니다"),
    ("파손의 위험이 있는 상품입니다. 주의해 주세요.", "파손의 위험이 있는 상품입니다. 주의해 주세요."),
)


class OrderList(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    location_name = models.CharField(max_length=20)
    order_name = models.CharField(max_length=20)
    phone_number = models.IntegerField(unique=False, null=True)
    order_request = models.CharField(max_length=50, choices=order_requests)
    location_zipcode = models.CharField(max_length=20)
    location_address = models.CharField(max_length=50)
    location_detail = models.CharField(max_length=50)


class OrderListFinal(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    location_name = models.CharField(max_length=20)
    order_name = models.CharField(max_length=20)
    phone_number = models.IntegerField(unique=False, null=True)
    order_request = models.CharField(max_length=50, choices=order_requests)
    product = models.TextField(blank=True)
    color = models.CharField(max_length=20, blank=True)
    size = models.CharField(max_length=20, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    location_zipcode = models.CharField(max_length=20)
    location_address = models.CharField(max_length=50)
    location_detail = models.CharField(max_length=50)
