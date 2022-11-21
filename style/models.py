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
    like_users = models.ManyToManyField(get_user_model(), related_name="like_style")
    hits = models.PositiveIntegerField(default=0, verbose_name='조회수')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    orderlists = models.CharField(null=True, max_length=100)

class Photo(models.Model):
    style = models.ForeignKey(Style, on_delete=models.CASCADE, null=True)
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        format="JPEG",
    )


class Style_Review(models.Model):
    content = models.TextField(max_length=50, verbose_name="댓글내용")
    style = models.ForeignKey(
        Style,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="style",
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name="댓글 작성자",
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="삭제여부")
    deleted = models.BooleanField(default=False, verbose_name="삭제 여부")

    def __str__(self):
        return self.content

    class Meta:
        db_table = "스타일 댓글"
        verbose_name = "스타일 댓글"
        verbose_name_plural = "스타일 댓글"
