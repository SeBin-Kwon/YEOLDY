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
    grades = (
        ("5", "5"),
        ("4", "4"),
        ("3", "3"),
        ("2", "2"),
        ("1", "1"),
    )
    grade = models.IntegerField(verbose_name="평점", choices=grades, default=0)
