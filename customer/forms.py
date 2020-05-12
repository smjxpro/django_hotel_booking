from django import forms

from authentication.models import User

from customer.models import Customer


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('nid_no', 'passport_no', 'phone_no')
