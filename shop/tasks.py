from celery.task import task
from django.core.mail import send_mail
from .models import Order
from .cart import Cart


# TODO:task send mail with order detailed info

@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order № {order.id}'
    message = f'''Dear {order.first_name},
    You have successfully placed an order.
    Your order: №{order.id}.'''
    mail_sent = send_mail(subject, message, 'emiliyasart@gmail.com', [order.email])
    return mail_sent
