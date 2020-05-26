"""django_hotel_booking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from rooms.views import room_type_list, index

urlpatterns = [
                  path('admin/', admin.site.urls),

                  path('', index, name='home'),

                  path('customer/', include('customer.urls')),
                  path('booking/', include('booking.urls')),
                  path('payment/', include('payment.urls')),
                  path('rooms/', include('rooms.urls')),
                  path('rooms/', room_type_list, name='rooms'),
                  path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
                  path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
                  path('services/', TemplateView.as_view(template_name='services.html'), name='services'),
                  path('cart/', TemplateView.as_view(template_name='cart.html'), name='cart'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
