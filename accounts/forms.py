from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm,
)
from .models import User
from django.forms import TextInput


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "nickname",
            "profile_image",
            "email",
            "birth",
            "phone_number",
            "gender",
        ]
        labels = {
            "profile_image": "프로필사진",
            "nickname": "이름",
            "username": "아이디",
            "password1": "비밀번호",
            "password2": "비밀번호확인",
            "email": "이메일주소",
            "phone_number": "휴대폰번호",
            "birth": "생일(6자리)",
            "gender": "성별",
        }


class CustomUserChangeForm(UserChangeForm):

    password = None

    class Meta:
        model = User
        fields = (
            "profile_image",
            "nickname",
            "username",
            "email",
            "phone_number",
            "birth",
            "gender",
        )
        labels = {
            "profile_image": "프로필사진",
            "nickname": "이름",
            "username": "아이디",
            "email": "이메일주소",
            "phone_number": "휴대폰번호",
            "birth": "생일",
            "gender": "성별",
        }
        widgets = {
            "username": TextInput(
                attrs={
                    "disabled": "disabled",
                }
            )
        }


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields["old_password"].label = "기존 비밀번호"
        self.fields["old_password"].widget.attrs.update(
            {
                "class": "details",
                "autofocus": False,
            }
        )
        self.fields["new_password1"].label = "새 비밀번호"
        self.fields["new_password1"].widget.attrs.update(
            {
                "class": "details",
            }
        )
        self.fields["new_password2"].label = "새 비밀번호 확인"
        self.fields["new_password2"].widget.attrs.update(
            {
                "class": "details",
            }
        )
