from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from clubkit.shop.models import Product
from clubkit.clubs.models import ClubInfo
from .cart import Cart, CartPackage
from .forms import CartAddProductForm
from clubkit.clubs.models import Packages


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    club_pk = request.session.get('pk')
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/details.html', {'cart': cart,
                                                 'club_pk': club_pk})


@require_POST
def cart_add_package(request, product_id):
    cart = CartPackage(request)
    product = get_object_or_404(Packages, id=product_id)
    cart.add(product=product)
    return redirect('cart:cart_detail_package')


def cart_remove_package(request, product_id):
    cart = CartPackage(request)
    product = get_object_or_404(Packages, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_add_package')


def cart_detail_package(request):
    cart = CartPackage(request)
    return render(request, 'club/package-detail.html', {'cart': cart,
                                                         })


