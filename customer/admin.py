from django.contrib import admin
from django.contrib.admin import ModelAdmin

from customer.models import Customer


class CustomerAdmin(ModelAdmin):
    list_display = (
        '__str__', 'name', 'phone_no', 'email')

    def email(self, obj):
        return obj.user.email

    def name(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'


admin.site.register(Customer, CustomerAdmin)
