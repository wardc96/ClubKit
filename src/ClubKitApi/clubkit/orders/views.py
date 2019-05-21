from django.shortcuts import render, redirect
from django.urls import reverse
from .models import OrderItem
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
    cart = Cart(request)
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
        club = ClubInfo.objects.filter(pk=club_pk)
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form,
                                                        })


def order_create_package(request):
    cart = Cart(request)
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
                                                        })


class ClubOrders(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'orders/order/club-orders.html'

    def get(self, request):
        club_pk = request.session.get('pk')
        club = ClubInfo.objects.filter(pk=club_pk)
        order = Order.objects.filter(club_id=club_pk)
        items = OrderItem.objects.get(order=order)
        return Response({'order': order,
                         'club_pk': club_pk,
                         'club': club,
                         'items': items
                         })

