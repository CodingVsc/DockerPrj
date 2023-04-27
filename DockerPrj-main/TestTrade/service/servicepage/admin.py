from django.contrib import admin

from servicepage.models import Service, Plan, Subscription

# Register your models here.
admin.site.register(Service)
admin.site.register(Plan)
admin.site.register(Subscription)