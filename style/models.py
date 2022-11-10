from django.db import models
from django.core.validators import FileExtensionValidator
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
    image = models.FileField(
        upload_to="images/",
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "png"])],
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tag = MultiSelectField(choices=STYLE_CATEGORY)
