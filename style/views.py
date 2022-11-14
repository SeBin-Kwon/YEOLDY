from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Style
from django.core.paginator import Paginator
from .form import StyleForm, ReviewForm


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
    if request.user == style.user:
        if request.method == "POST":
            style_form = StyleForm(request.POST, request.FILES, instance=style)
            if style_form.is_valid():
                style_form.save()
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
    review_form = ReviewForm()
    page = request.GET.get("page", "1")
    reviews = style.style_review_set.all().order_by("-pk")
    paginator = Paginator(reviews, "5")
    page_obj = paginator.get_page(page)

    context = {
        "style": style,
        "review_form": review_form,
        "review_list": page_obj,
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


@login_required
def review_create(request, pk):
    if request.method == "POST":
        style = Style.objects.get(pk=pk)
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.style = style
            review.save()
            return redirect("style:detail", style.pk)
