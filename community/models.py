from django.db import models
from django.core.validators import FileExtensionValidator
from imagekit.models import ProcessedImageField
from products.models import Products
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.


class QnA(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.FileField(
        upload_to="images/",
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "png"])],
        blank=True,
    )
    solve = models.BooleanField(default=False)
    Product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    password = models.CharField(max_length=20, blank=True, null=True)
    hits = models.PositiveIntegerField(default=0, verbose_name="조회수")


class QnA_Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    QnA = models.ForeignKey(QnA, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)


class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    RATING = [
        (1, "⭐"),
        (2, "⭐⭐"),
        (3, "⭐⭐⭐"),
        (4, "⭐⭐⭐⭐"),
        (5, "⭐⭐⭐⭐⭐"),
    ]
    grade = models.IntegerField(choices=RATING, default=None)

    def __str__(self):
        return self.title


class Photo(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, null=True)
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        format="JPEG",
    )
