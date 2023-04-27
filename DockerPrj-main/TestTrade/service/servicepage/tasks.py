from celery import shared_task



@shared_task
def set_price(subscription_id):
    from servicepage.models import Subscription

    subscription = Subscription.objects.get(id=subscription_id)
    new_price = (subscription.service_sub.full_price -
                 subscription.service_sub.full_price * (subscription.sub_plan.discount_percent / 100))
    subscription.price = new_price
    subscription.save()
