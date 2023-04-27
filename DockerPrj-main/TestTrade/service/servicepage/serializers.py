from rest_framework import serializers

from servicepage.models import Subscription, Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('__all__')


class SubscriptionSerializer(serializers.ModelSerializer):
    plan = PlanSerializer
    email = serializers.CharField(source='client.user.email')
    price = serializers.SerializerMethodField()

    def get_price(self, instance):
        return instance.price


    class Meta:
        model = Subscription
        fields = ('id', 'sub_plan_id', 'email', 'sub_plan', 'price')