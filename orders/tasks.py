from celery import task
from django.core.mail import send_mail
from .models import Order
from myshopConfig import settings

@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = 'Dear {},\n\nYou have successfully placed an order.\
        Your order id is {}.'.format(order.first_name, order.id)

    mail_sent = send_mail(subject, message,
                            settings.EMAIL_HOST_USER,
                            [order.email])
    return mail_sent