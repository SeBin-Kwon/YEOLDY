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

app_name = "products"

urlpatterns = [
    path("create/", views.create, name="create"),
    path("index/", views.index, name="index"),
    path("index/1/", views.index_1, name="index_1"),
    path("index/2/", views.index_2, name="index_2"),
    path("index/3/", views.index_3, name="index_3"),
    path("index/4/", views.index_4, name="index_4"),
    path("index/5/", views.index_5, name="index_5"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/detail/", views.detail, name="detail"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:product_pk>/save/", views.save, name="save"),
    path("search/", views.search, name="search"),
    path("search_main/", views.search_main, name="search_main"),
    path("new_products/", views.new_products, name="new_products"),
]
