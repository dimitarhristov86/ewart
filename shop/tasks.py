from celery.task import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order № {order.id}'
    message = f'''Dear {order.first_name} {order.last_name},
    You have successfully placed an order at Emiliya's art shop.
    Your order: №{order.id}.
    Payment pending....
    IBAN: 11111111111(example)
    Owner IBAN: Emiliya's art shop
    IMPORTANT!!!
    Please provide an order number at required info for payment!
    Your order will be shipped to your address( {order.address}, {order.city} ) provided in order form after successful payment!
    For any questions about your order, please use contact form on our website.
    Thank you for your purchase!
    Sincerely Emiliya Ivanova'''
    mail_sent = send_mail(subject, message, 'emiliyasart@gmail.com', [order.email])
    return mail_sent
