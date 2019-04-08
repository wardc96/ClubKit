from celery import task
from django.conf import settings
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    """
    Task to send an email notification when an order is created
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order_id)
    message = 'Dear {},\n\nYou have successfully placed an order. Your order id is {}.'.format(order.first_name, order.id)
    from_email = settings.EMAIL_HOST_USER
    to_email = [order.email]
    send_mail(subject,message,from_email,to_email)
    return send_mail


