from django.db import models
from django.core.validators import FileExtensionValidator
from products.models import Products
from django.contrib.auth import get_user_model


# Create your models here.


class QnA(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.FileField(
        upload_to="images/",
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "png"])],
    )
    solve = models.BooleanField(default=False)
    Product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.FileField(
        upload_to="images/",
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "png"])],
    )
    # Product = models.ForeignKey()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    RATING = [
        (1, "★"),
        (2, "★★"),
        (3, "★★★"),
        (4, "★★★★"),
        (5, "★★★★★"),
    ]
    grade = models.IntegerField(choices=RATING, default=None)
