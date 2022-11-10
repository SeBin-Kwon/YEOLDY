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
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path,include
=======
from django.urls import path, include
>>>>>>> cb6b013efa33b76024efb4f9c0ef64094229dea1
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('admin/', admin.site.urls),
    path('', views.main, name='name'),
    path('community/', include('community.urls')),
=======
    path("admin/", admin.site.urls),
    path("", views.main, name="name"),
    path("products/", include("products.urls")),
    path('accounts/', include('accounts.urls')),
>>>>>>> cb6b013efa33b76024efb4f9c0ef64094229dea1
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
