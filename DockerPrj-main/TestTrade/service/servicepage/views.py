from django.db.models import Prefetch, F, Sum
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from clients.models import Client
from servicepage.models import Subscription
from servicepage.serializers import SubscriptionSerializer


# Create your views here.
class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().prefetch_related(
        'sub_plan',
        Prefetch('client', queryset=Client.objects.all().select_related('user').only('user__email'))
    )#.annotate(price=F('service_sub__full_price') -
                     #F('service_sub__full_price') *
                     #F('sub_plan__discount_percent') / 100.00)
    serializer_class = SubscriptionSerializer

    def list(self, request, *args, **kwargs): #переопределяем метод list(так делать не надо :) либо согласовывайте это с фронтом своим)
        queryset = self.filter_queryset(self.get_queryset())
        response = super().list(request, *args, **kwargs)

        response_data = {'result': response.data}
        response_data['total_amount'] = queryset.aggregate(total=Sum('price')).get('total')
        response.data = response_data
        return response