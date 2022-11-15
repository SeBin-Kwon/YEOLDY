from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Products, Search
from django.http import JsonResponse
from .form import ProductsForm
from django.db.models import F  # 검색 순위 조회수 증가
from django.db.models import Q  # 검색 기능

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
    reviews = product.review_set.all().order_by("-pk")
    colors = list(str(product.color).split(", "))
    sizes = list(str(product.size).split(", "))
    context = {
        "reviews": reviews,
        "product": product,
        "review_list": reviews,
        "colors": colors,
        "sizes": sizes,
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
        is_saved = False
    else:
        product.save_users.add(request.user)
        is_saved = True
    context = {"issaved": is_saved}
    return JsonResponse(context)


# 검색 기능
def search(request):
    search_ranking = Search.objects.order_by("-search_count")
    products = Products.objects.all().order_by("-pk")
    search = request.GET.get("search")
    search_create = Search.objects.filter(search_text=search)
    search_ranking = Search.objects.order_by("-search_count")[:5]  # 순위 5
    if search:
        products = Products.objects.filter(
            Q(name__icontains=search) | Q(category__icontains=search)
        )
    if search_create:
        search_exist = Search.objects.get(search_text=search)
        search_exist.search_count += 1
        search_exist.save()
    else:
        Search.objects.create(search_text=search)
    context = {
        'products':products,
        "search_ranking": search_ranking,
        "search": search,
        "products": products,
    }
    return render(request, "products/search.html", context)


def search_main(request):
    search_ranking = Search.objects.order_by("-search_count")[:5]
    context = {
        "search_ranking": search_ranking,
    }

    return render(request, "products/search_main.html", context)
