from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Style, Style_Review, Photo
from .form import StyleForm, ReviewForm
from products.models import Products
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q  # 검색 기능
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder


def index(request):
    styles = Style.objects.order_by("-pk")
    context = {
        "styles": styles,
    }
    return render(request, "style/index.html", context)


@login_required
def create(request):
    if request.method == "POST":
        style_form = StyleForm(request.POST, request.FILES)
        if style_form.is_valid():
            style = style_form.save(commit=False)
            style.user = request.user
            style.save()
            for img in request.FILES.getlist("imgs"):
                photo = Photo()
                photo.style = style
                photo.image = img
                photo.save()
            return redirect("style:index")
    else:
        style_form = StyleForm()
    context = {
        "style_form": style_form,
    }
    return render(request, "style/form.html", context)


@login_required
def update(request, pk):
    style = Style.objects.get(id=pk)
    photo = style.photo_set.all()
    if request.user == style.user:
        if request.method == "POST":
            photo.delete()
            style_form = StyleForm(request.POST, request.FILES, instance=style)
            if style_form.is_valid():
                style_form.save()
                for img in request.FILES.getlist("imgs"):
                    photo = Photo()
                    photo.style = style
                    photo.image = img
                    photo.save()
                return redirect("style:detail", style.pk)

        else:
            style_form = StyleForm(instance=style)
        context = {
            "style_form": style_form,
        }

        return render(request, "style/form.html", context)
    else:
        return redirect("style:detail", style.pk)


def detail(request, pk):
    style = Style.objects.get(pk=pk)
    style_image = style.photo_set.all()
    review_form = ReviewForm()
    reviews = style.style_review_set.all().order_by("-pk")
    context = {
        "style": style,
        "review_form": review_form,
        "reviews": reviews,
        "style_images": style_image,
    }
    return render(request, "style/detail.html", context)


@login_required
def delete(request, pk):
    style = Style.objects.get(pk=pk)
    if request.user == style.user:
        style.delete()
        return redirect("style:index")
    else:
        return redirect("style:detail", pk)


# @login_required
# def review_create(request, pk):
#     if request.method == "POST":
#         style = Style.objects.get(pk=pk)
#         review_form = ReviewForm(request.POST)
#         if review_form.is_valid():
#             review = review_form.save(commit=False)
#             review.user = request.user
#             review.style = style
#             review.save()
#             return redirect("style:detail", style.pk)


@login_required
def review_create(request, pk):
    style = get_object_or_404(Style, id=pk)
    user = request.POST.get("user")
    content = request.POST.get("content")
    if content:
        review = Style_Review.objects.create(
            style=style,
            content=content,
            user=request.user,
        )
        style.save()
        data = {
            "user": user,
            "content": content,
            "created": "방금 전",
            "review_id": review.id,
        }
        if request.user == style.user:
            data["self_comment"] = "(작성자)"

        return HttpResponse(
            json.dumps(data, cls=DjangoJSONEncoder), content_type="application/json"
        )


@login_required
def review_delete(request, pk):
    style = get_object_or_404(Style, id=pk)
    review_id = request.POST.get("review_id")
    target_review = Style_Review.objects.get(pk=review_id)

    if (
        request.user == target_review.user
        or request.user.level == "1"
        or request.user.level == "0"
    ):
        target_review.deleted = True
        target_review.save()
        style.save()
        data = {
            "review_id": review_id,
        }
        return HttpResponse(
            json.dumps(data, cls=DjangoJSONEncoder), content_type="application/json"
        )


@login_required
def like(request, style_pk):
    style = Style.objects.get(pk=style_pk)

    if request.user in style.like_users.all():
        style.like_users.remove(request.user)
        is_liked = False
    else:
        style.like_users.add(request.user)
        is_liked = True
    context = {"isliked": is_liked}
    return JsonResponse(context)
