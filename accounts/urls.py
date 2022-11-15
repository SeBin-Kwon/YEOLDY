"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("callback/", views.callback, name="callback"),
    path("logout/", views.logout, name="logout"),
    path("mypage/<int:pk>/", views.mypage, name="mypage"),
    path("mypage-update/<int:pk>/", views.mypage_update, name="mypage-update"),
    path("mypage-delete/<int:pk>/", views.mypage_delete, name="mypage-delete"),
    path("change-password/", views.change_password, name="change-password"),
    path("database/", views.database, name="database"),
    path("database/naver/", views.database_naver, name="databse_naver"),
    path("<int:pk>/follow/", views.follow, name="follow"),
]
