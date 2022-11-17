from django.shortcuts import render, redirect
from products.models import Products
from .models import CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


@login_required
def add_cart(request, product_id):
    product = Products.objects.get(id=product_id)
    if request.method == "POST":
        cart_quantity = request.POST["cart_quantity"]
        color = request.POST["color"]
        size = request.POST["size"]
        print(cart_quantity)
        print(color)
        print(size)
        # 장바구니에 들어가는 product
        img = product.photo_set.filter(product_id=product_id)[0].image
        product.image = img
        product.save()

    # cart_item이 있는지 없는지 여부 확인
    try:
        # size와 color까지 같은 애들은 수량만 증가해줌
        cart_item = CartItem.objects.get(
            product=product, color=color, size=size, user=request.user
        )
        cart_item.quantity += int(cart_quantity)
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=int(cart_quantity),
            color=color,
            size=size,
            user=request.user,
        )
        cart_item.save()
    return redirect("cart:cart_detail")


# counter=0 : 루프가 입력된 횟수(인덱스)
@login_required
def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart_items = CartItem.objects.filter(user=request.user)
        for cart_item in cart_items:
            # 총 가격과 총 개수를 계산
            total += cart_item.product.cost * cart_item.quantity
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    return render(
        request,
        "cart/cart.html",
        {
            "cart_items": cart_items,
            "total": total,
            "counter": counter,
            "cart_length": len(cart_items),
        },
    )


@login_required
def delete_cart(request, product_id, product_color, product_size):
    # 해당 유저, 상품, 가격, 사이즈까지 모두 같은 애들만 삭제
    cart_item = CartItem.objects.get(
        id=product_id, color=product_color, size=product_size, user=request.user
    )
    cart_item.delete()
    return redirect("cart:cart_detail")


@login_required
def clear_cart(request):
    # 해당 유저의 item들을 모두 삭제
    cart_items = CartItem.objects.filter(user=request.user)
    cart_items.delete()
    return redirect("cart:cart_detail")


@login_required
def revise_cart(request, product_id, product_color, product_size):
    if request.method == "POST":
        cart_quantity = request.POST["cart_quantity"]
        print(cart_quantity)
    # 장바구니에 들어가는 product
    product = Products.objects.get(id=product_id)

    cart_item = CartItem.objects.get(
        product=product, color=product_color, size=product_size, user=request.user
    )
    cart_item.quantity = int(cart_quantity)
    cart_item.save()

    return redirect("cart:cart_detail")
