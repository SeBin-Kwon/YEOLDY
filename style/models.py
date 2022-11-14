from django.db import models
from django.core.validators import FileExtensionValidator
from imagekit.models import ProcessedImageField
from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField

STYLE_CATEGORY = (
    ("캐주얼룩", "캐주얼룩"),
    ("데이트룩", "데이트룩"),
    ("포멀룩", "포멀룩"),
    ("스트릿룩", "스트릿룩"),
    ("걸리쉬룩", "걸리쉬룩"),
)


class Style(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        format="JPEG",
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tag = MultiSelectField(choices=STYLE_CATEGORY)
