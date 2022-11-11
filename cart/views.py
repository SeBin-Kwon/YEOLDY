from django.shortcuts import render, redirect
from products.models import Products
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def _cart_id(request):
    #각 상품에 대해 유저의 session_key가 있는지 확인
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    #장바구니에 들어가는 product
    product = Products.objects.get(id=product_id)
    try:
        #해당 상품에 유저의 session_key가 있는지 확인하고
        cart = Cart.objects.get(cart_id=_cart_id(request))
    #cart가 없다면,
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()

    #cart_item이 있는지 없는지 여부 확인
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart
        )
        cart_item.save()
    return redirect('cart:cart_detail')

#counter=0 : 루프가 입력된 횟수(인덱스)
def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.cost * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total': total, 'counter': counter})

def delete_cart(request, product_id):
    cart_item = CartItem.objects.get(id=product_id)
    cart_item.delete()
    return redirect('cart:cart_detail')

def clear_cart(request):
    cart_items = CartItem.objects.all()
    cart_items.delete()
    return redirect('cart:cart_detail')