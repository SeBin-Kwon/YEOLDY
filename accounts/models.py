from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

# Create your models here.
class User(AbstractUser):
    profile_image = models.ImageField(upload_to="images/", blank=True)
    nickname = models.CharField(max_length=20)
    phone_number = PhoneNumberField(unique=True, null=True, blank=True, region="KR")
    birth = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(991231),
        ],
    )
    genders = (
        ("M", "남성"),
        ("W", "여성"),
    )
    gender = models.CharField(
        verbose_name="성별", max_length=1, choices=genders, null=True
    )
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )
    # like = models.ManyToManyField()
