from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model


# Create your models here.
class User(AbstractUser):
    phone_number = PhoneNumberField(unique=True, null=False, blank=False, region="KR")
    birth = models.IntegerField()
    sex = models.BooleanField(default=False)
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )
    # like = models.ManyToManyField()


class Basket(models.Model):
    # product = models.ForeignKey()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
