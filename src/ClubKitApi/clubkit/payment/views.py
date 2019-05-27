from decimal import Decimal
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
from clubkit.orders.models import Order
from clubkit.clubs.models import ClubInfo
from django.views.decorators.csrf import csrf_exempt
from clubkit.cart.cart import Cart


@csrf_exempt
def payment_done(request):
    club_pk = request.session.get('pk')
    club = ClubInfo.objects.filter(pk=club_pk)
    # order_id = request.session.get('order_id')
    # set_paid = Order.objects.filter(pk=order_id)
    # set_paid.paid = True
    # set_paid.save(update_fields=["paid"])
    return render(request, 'payment/done.html', {'club': club,
                                                 # 'order_id': order_id,
                                                 # 'set_paid': set_paid
                                                 })


@csrf_exempt
def payment_canceled(request):
    club_pk = request.session.get('pk')
    club = ClubInfo.objects.filter(pk=club_pk)
    return render(request, 'payment/canceled.html', {'club': club,
                                                     })


def payment_process(request):
    hidecart = True
    club_pk = request.session.get('pk')
    club = ClubInfo.objects.filter(pk=club_pk)
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    host = request.get_host()
    # club_paypal = request.session.get('paypal_email')

    paypal_dict = {
        'business': '',
        'amount': '%.2f' % order.get_total_cost().quantize(Decimal('.01')),
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'EUR',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment:done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment:canceled')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payment/process.html', {'order': order,
                                                    'form': form,
                                                    'club_pk': club_pk,
                                                    'club': club,
                                                    'hidecart': hidecart})
