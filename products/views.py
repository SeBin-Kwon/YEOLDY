from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Products, Search, Photo
from django.http import JsonResponse
from .form import ProductsForm
from django.db.models import F  # 검색 순위 조회수 증가
from django.db.models import Q  # 검색 기능
from community.models import Review as review

# Create your views here.

# 상품 리스트 기능(메인페이지로 대체?)카테고리전체
def index(request):
    products = Products.objects.all().order_by("-pk")
    context = {
        "products": products,
    }
    return render(request, "products/index.html", context)


# 카테고리 별
def index_1(request):
    products = Products.objects.filter(category="상의")
    context = {
        "products": products,
    }
    return render(request, "products/index.html", context)


def index_2(request):
    products = Products.objects.filter(category="하의")
    context = {
        "products": products,
    }
    return render(request, "products/index.html", context)


def index_3(request):
    products = Products.objects.filter(category="아우터")
    context = {
        "products": products,
    }
    return render(request, "products/index.html", context)


def index_4(request):
    products = Products.objects.filter(category="신발")
    context = {
        "products": products,
    }
    return render(request, "products/index.html", context)


def index_5(request):
    products = Products.objects.filter(category="악세사리")
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
            for img in request.FILES.getlist("imgs"):
                photo = Photo()
                photo.product = product
                photo.image = img
                photo.save()
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
                for img in request.FILES.getlist("imgs"):
                    photo = Photo()
                    photo.product = product
                    photo.image = img
                    photo.save()
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
    product_images = product.photo_set.all()
    reviews = product.review_set.all().order_by("-pk")
    points = 0
    for review in reviews:
        points += review.grade
    if len(reviews):
        points = round(points / len(reviews), 1)

    product.average_rating = points
    product.save()

    qnas = product.qna_set.all().order_by("-pk")
    colors = list(str(product.color).split(", "))
    sizes = list(str(product.size).split(", "))

    context = {
        "reviews": reviews,
        "qnas": qnas,
        "product": product,
        "review_list": reviews,
        "colors": colors,
        "sizes": sizes,
        "product_images": product_images,
        "points": points,
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
    products = Products.objects.all().order_by("-pk")
    search = request.GET.get(
        "search",
    )
    search_create = Search.objects.filter(search_text=search)
    search_ranking = Search.objects.order_by("-search_count")[:5]  # 순위
    if search:
        products = Products.objects.filter(
            Q(name__icontains=search) | Q(category__icontains=search)
        ).order_by("-pk")
    if search_create:
        search_exist = Search.objects.get(search_text=search)
        if products:
            search_exist.search_count += 1  # 있다면 +1  # 없다면 0
            search_exist.save()
    else:
        if products:
            Search.objects.create(search_text=search)
    context = {
        "products": products,
        "search_ranking": search_ranking,
        "search": search,
    }
    return render(request, "products/search_main.html", context)


def search_main(request):
    search_ranking = Search.objects.order_by("-search_count")[:5]
    context = {
        "search_ranking": search_ranking,
    }
    return render(request, "products/search_main.html", context)


# 새상품
def new_products(request):
    new_products = Products.objects.filter(Q(new_product="1"))
    context = {
        "new_products": new_products,
    }
    return render(request, "products/new_products.html", context)


# 베스트 상품
def best_products(request):
    best_products = Products.objects.filter(average_rating__isnull=False).order_by(
        "-average_rating"
    )[
        :5
    ]  # top5/NULL제외
    best_products_1 = Products.objects.filter(
        average_rating__isnull=False, category="상의"
    ).order_by("-average_rating")[
        :5
    ]  # 상의top/5/NULL제외
    best_products_2 = Products.objects.filter(
        average_rating__isnull=False, category="하의"
    ).order_by("-average_rating")[
        :5
    ]  # 하의top5/NULL제외
    best_products_3 = Products.objects.filter(
        average_rating__isnull=False, category="아우터"
    ).order_by("-average_rating")[
        :5
    ]  # 아우터top5/NULL제외
    best_products_4 = Products.objects.filter(
        average_rating__isnull=False, category="신발"
    ).order_by("-average_rating")[
        :5
    ]  # 신발top5/NULL제외
    best_products_5 = Products.objects.filter(
        average_rating__isnull=False, category="악세사리"
    ).order_by("-average_rating")[
        :5
    ]  # 악세사리top5/NULL제외
    context = {
        "best_products": best_products,
        "best_products_1": best_products_1,
        "best_products_2": best_products_2,
        "best_products_3": best_products_3,
        "best_products_4": best_products_4,
        "best_products_5": best_products_5,
    }
    return render(request, "products/best_products.html", context)
