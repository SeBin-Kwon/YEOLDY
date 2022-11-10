from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Products
from .form import ProductsForm

# Create your views here.


def index(request):
    products = Products.objects.order_by("-pk")
    context = {
        "products": products,
    }
    return render(request, "products/index.html", context)


def create(request):
    if request.method == "POST":
        products_form = ProductsForm(request.POST, request.FILES)
        if products_form.is_valid():
            products_form.save()
            return redirect("products:index")

    else:
        products_form = ProductsForm()
        context = {
            "products_form": products_form,
        }
        return render(request, "products/create.html", context)


def update(request, pk):
    product = Products.objects.get(id=pk)

    if request.method == "POST":
        products_form = ProductsForm(request.POST, request.FILES, instance=product)
        if products_form.is_valid():
            products_form.save()
            return redirect("products:detail", product.pk)

    else:
        products_form = ProductsForm(instance=product)
    context = {
        "products_form": products_form,
    }

    return render(request, "products/update.html", context)


def detail(request, pk):
    product = Products.objects.get(pk=pk)

    context = {
        "product": product,
    }
    return render(request, "products/detail.html", context)


def delete(request, pk):
    product = Products.objects.get(pk=pk)
    product.delete()
    return redirect("products:index")
