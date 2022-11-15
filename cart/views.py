from django.shortcuts import render, redirect
from products.models import Products
from .models import CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

@login_required
def add_cart(request, product_id):
    if request.method == "POST":
        cart_quantity = request.POST["cart_quantity"]
        print(cart_quantity)
    # 장바구니에 들어가는 product
    product = Products.objects.get(id=product_id)

    # cart_item이 있는지 없는지 여부 확인
    try:
        cart_item = CartItem.objects.get(product=product, user=request.user)
        cart_item.quantity += int(cart_quantity)
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product, quantity=int(cart_quantity), user=request.user
        )
        cart_item.save()
    return redirect("cart:cart_detail")

# counter=0 : 루프가 입력된 횟수(인덱스)
@login_required
def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart_items = CartItem.objects.filter(user=request.user)
        for cart_item in cart_items:
            total += cart_item.product.cost * cart_item.quantity
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    return render(
        request,
        "cart/cart.html",
        {"cart_items": cart_items, "total": total, "counter": counter},
    )

@login_required
def delete_cart(request, product_id):
    cart_item = CartItem.objects.get(id=product_id, user=request.user)
    cart_item.delete()
    return redirect("cart:cart_detail")

@login_required
def clear_cart(request):
    cart_items = CartItem.objects.get(user=request.user)
    cart_items.delete()
    return redirect("cart:cart_detail")
