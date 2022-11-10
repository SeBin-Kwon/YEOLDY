from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'nickname', 'profile_image', 'email', 'birth', 'phone_number', 'gender']
        labels = {
            'profile_image': '프로필사진',
            'nickname': '이름',
            'username': '아이디',
            'password1': '비밀번호',
            'password2': '비밀번호확인',
            'email': '이메일주소',
            'phone_number': '휴대폰번호',
            'birth': '생일',
            'gender': '성별'
        }

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('profile_image', 'nickname', 'username', 'email', 'phone_number', 'birth', 'gender')
        labels = {
            'profile_image': '프로필사진',
            'nickname': '이름',
            'username': '아이디',
            'email': '이메일주소',
            'phone_number': '휴대폰번호',
            'birth': '생일',
            'gender': '성별'
        }