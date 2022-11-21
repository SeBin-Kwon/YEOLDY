from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField


MY_COLOR = (
    ("화이트", "화이트"),
    ("블랙", "블랙"),
    ("베이지", "베이지"),
    ("카키", "카키"),
    ("차콜", "차콜"),
    ("그레이", "그레이"),
    ("그린", "그린"),
    ("레드", "레드"),
    ("핫핑크", "핫핑크"),
    ("퍼플", "퍼플"),
    ("블루", "블루"),
    ("크림", "크림"),
    ("라이트퍼플", "라이트퍼플"),
)

MY_SIZE = (
    (220, 220),
    (230, 230),
    (240, 240),
    (250, 250),
    (260, 260),
    (270, 270),
    (280, 280),
    ("XS", "XS"),
    ("S", "S"),
    ("M", "M"),
    ("L", "L"),
    ("XL", "XL"),
    ("XXL", "XXL"),
    ("FREE", "FREE"),
)

MY_CATEGORY = (
    ("상의", "상의"),
    ("하의", "하의"),
    ("아우터", "아우터"),
    ("신발", "신발"),
    ("악세사리", "악세사리"),
)


class Products(models.Model):
    name = models.CharField(max_length=20)
    cost = models.IntegerField()
    cost_2 = models.IntegerField(null=True)
    category = models.CharField(max_length=10, choices=MY_CATEGORY)
    color = MultiSelectField(choices=MY_COLOR)
    size = MultiSelectField(choices=MY_SIZE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        format="JPEG",
    )
    save_users = models.ManyToManyField(get_user_model(), related_name="save_products")
    new_product = models.BooleanField(default=False)
    average_rating = models.FloatField(null=True)
    sale_percent = models.IntegerField(null=True)


class Photo(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        format="JPEG",
    )


class Search(models.Model):
    search_count = models.IntegerField(default=1)
    search_text = models.CharField(max_length=20)
