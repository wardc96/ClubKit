from django.shortcuts import render, redirect
from django.urls import reverse
from .models import OrderItem, Order
from .forms import OrderCreateForm
from .tasks import order_created
from clubkit.cart.cart import Cart
from clubkit.clubs.models import Pitch, ClubInfo
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from clubkit.clubs.models import ClubInfo


def order_create(request):
    hidecart = False
    cart = Cart(request)
    club_pk = request.session.get('pk')
    club = ClubInfo.objects.filter(pk=club_pk)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            # clear the cart

            cart.clear()

            # launch asynchronous task

            order_created.delay(order.id)

            # set the order in the session

            request.session['order_id'] = order.id

            # redirect to the payment

            return redirect(reverse('payment:process'))
    else:
        club_pk = request.session.get('pk')
        club = ClubInfo.objects.filter(pk=club_pk)
        inital_data = {
            'club_id': club_pk
        }
        form = OrderCreateForm(initial=inital_data)
    return render(request, 'orders/order/create.html', {'form': form,
                                                        'club': club,
                                                        'cart': cart,
                                                        'hidecart': hidecart
                                                        })


def order_create_package(request):
    hidecart = False
    cart = Cart(request)
    club_pk = request.session.get('pk')
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            # clear the cart

            cart.clear()

            # launch asynchronous task

            order_created.delay(order.id)

            # set the order in the session

            request.session['order_id'] = order.id

            # redirect to the payment

            return redirect(reverse('payment:process'))
    else:
        club_pk = request.session.get('pk')
        inital_data = {
            'club_id': club_pk
        }
        form = OrderCreateForm(initial=inital_data)
    return render(request, 'orders/order/package-create.html', {'form': form,
                                                                'club_pk': club_pk,
                                                                'cart': cart,
                                                                'hidecart': hidecart
                                                                })


class ClubOrders(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'orders/order/club-orders.html'

    def get(self, request):
        club_pk = request.session.get('pk')
        club = ClubInfo.objects.filter(pk=club_pk)
        order = Order.objects.filter(club_id=club_pk, complete=False)
        # items = OrderItem.objects.filter(order__in=order)
        return Response({'order': order,
                         'club_pk': club_pk,
                         'club': club,
                         # 'items': items
                         })


def view_order(request, pk):
    club_pk = request.session.get('pk')
    club = ClubInfo.objects.filter(pk=club_pk)
    order_id = OrderItem.objects.filter(order=pk)
    return render(request, 'orders/order/view_order.html', {'order_id': order_id,
                                                            'club': club})


def complete_order(request, pk):
    club_pk = request.session.get('pk')
    club = ClubInfo.objects.filter(pk=club_pk)
    order = Order.objects.filter(club_id=club_pk, complete=False)
    order_id = Order.objects.filter(pk=pk)
    order_id.update(complete=True)
    return render(request, 'orders/order/club-orders.html', {'order': order,
                                                             'club': club})


def completed_orders(request):
    club_pk = request.session.get('pk')
    club = ClubInfo.objects.filter(pk=club_pk)
    order = Order.objects.filter(club_id=club_pk, complete=True)
    return render(request, 'orders/order/complete_orders.html',
                  {'order': order,
                   'club_pk': club_pk,
                   'club': club})


def uncomplete_order(request, pk):
    club_pk = request.session.get('pk')
    club = ClubInfo.objects.filter(pk=club_pk)
    order = Order.objects.filter(club_id=club_pk, complete=True)
    order_id = Order.objects.filter(pk=pk)
    order_id.update(complete=False)
    return render(request, 'orders/order/complete_orders.html', {'order': order,
                                                                 'club': club})