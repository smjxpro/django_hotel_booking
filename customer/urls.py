from django.urls import path
from django.views.generic import TemplateView

from customer.views import *

app_name = 'customer'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('dashboard/', customer_dashboard, name='dashboard'),

]
