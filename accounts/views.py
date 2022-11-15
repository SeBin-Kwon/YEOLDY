from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib.auth import update_session_auth_hash
from django.http import JsonResponse
import json
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    return render(request, "accounts/index.html")


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    print(form.errors)
    return render(request, "accounts/signup.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("main")
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


def callback(request):
    return render(request, "accounts/callback.html")


def logout(request):
    auth_logout(request)
    print("로그아웃 완료")
    return redirect("main")


def mypage(request, pk):
    user = User.objects.get(pk=pk)
    context = {
        "user": user,
    }
    return render(request, "accounts/mypage.html", context)


@login_required
def mypage_update(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("accounts:mypage", user.pk)
    else:
        form = CustomUserChangeForm(instance=user)
    context = {"form": form}
    return render(request, "accounts/mypage_update.html", context)


@login_required
def mypage_delete(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect("accounts:index")


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        print(request.POST)
        if form.is_valid():
            print(1)
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("accounts:mypage", request.user.pk)
    else:
        print(2)
        form = PasswordChangeForm(request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/change_password.html", context)


def database(request):
    jsonObject = json.loads(request.body)
    username = jsonObject.get("username")
    users = User.objects.filter(username=username)

    if users:
        user = User.objects.get(username=username)
        auth_login(request, user)
    else:
        user = User()
        user.username = jsonObject.get("username")
        user.email = jsonObject.get("email")
        user.gender = jsonObject.get("gender")
        user.save()
        user = User.objects.get(username=username)
        auth_login(request, user)
    return JsonResponse(
        {"username": user.username, "email": user.email, "gender": user.gender}
    )


def database_naver(request):
    jsonObject = json.loads(request.body)
    username = jsonObject.get("id")

    users = User.objects.filter(username=username)
    if users:
        user = User.objects.get(username=username)
        auth_login(request, user)

    else:
        user = User()
        user.username = jsonObject.get("id")

        user.nickname = jsonObject.get("name")
        user.email = jsonObject.get("email")
        # user.phone = jsonObject.get('mobile')
        user.save()
        user = User.objects.get(username=username)
        auth_login(request, user)
    return JsonResponse({"username": user.username, "email": user.email})


def follow(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)

    # 스스로를 팔로우하려는 경우
    if request.user == user:
        return redirect("accounts:index")
    # 팔로우하고 있는 상태인 경우
    if request.user in user.followers.all():
        user.followers.remove(request.user)
        is_followed = False
    # 팔로우하고 있지 않았을때
    else:
        user.followers.add(request.user)
        is_followed = True
    context = {
        "is_followed": is_followed,
        "followers_count": user.followers.count(),
        "followings_count": user.followings.count(),
    }
    return JsonResponse(context)
