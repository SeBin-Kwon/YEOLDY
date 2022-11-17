from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField


MY_COLOR = (
    ("white", "white"),
    ("black", "black"),
    ("beige", "beige"),
    ("khaki", "khaki"),
    ("charcoal", "charcoal"),
    ("gray", "gray"),
    ("green", "green"),
    ("yellow", "yellow"),
    ("red", "red"),
    ("pink", "pink"),
    ("blue", "blue"),
)

MY_SIZE = (
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
    new_product  = models.BooleanField(default=False)

class Search(models.Model):
    search_count = models.IntegerField(default=1)
    search_text = models.CharField(max_length=20)
