from django.shortcuts import render
from products.models import Products


def main(request):
    # 전체 상품 top 5
    best_products = Products.objects.filter(average_rating__isnull=False).order_by(
        "-average_rating"
    )[:5]
    context = {
        "best_products": best_products,
    }

    return render(request, "main.html", context)
