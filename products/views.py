from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Products
from .form import ProductsForm


# Create your views here.

# 상품 리스트 기능(메인페이지로 대체?)
def index(request):
    products = Products.objects.order_by("-pk")
    context = {
        "products": products,
    }
    return render(request, "products/index.html", context)


# 상품 등록 기능
@login_required
def create(request):
    if request.method == "POST":
        products_form = ProductsForm(request.POST, request.FILES)
        if products_form.is_valid():
            product = products_form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect("products:index")

    else:
        products_form = ProductsForm()
        context = {
            "products_form": products_form,
        }
        return render(request, "products/form.html", context)


# 상품 등록 수정 기능
@login_required
def update(request, pk):
    product = Products.objects.get(id=pk)
    if request.user == product.user:
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

        return render(request, "products/form.html", context)
    else:
        return redirect("products:detail", product.pk)


# 상품 디테일 연결 기능
def detail(request, pk):
    product = Products.objects.get(pk=pk)

    context = {
        "product": product,
    }
    return render(request, "products/detail.html", context)


# 상품 등록 삭제
@login_required
def delete(request, pk):
    product = Products.objects.get(pk=pk)
    if request.user == product.user:
        product.delete()
        return redirect("products:index")
    else:
        return redirect("products:detail", pk)


# 찜하기 기능
@login_required
def save(request, product_pk):
    product = Products.objects.get(pk=product_pk)

    if request.user in product.save_users.all():
        product.save_users.remove(request.user)
    else:
        product.save_users.add(request.user)

    return redirect("products:detail", product_pk)
