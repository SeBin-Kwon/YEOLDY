from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Style
from django.core.paginator import Paginator
from .form import StyleForm


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
