from django.db import models

from authentication.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, related_name='customer', on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=13, verbose_name='Phone No')
    nid_no = models.CharField(max_length=32, verbose_name='NID No')
    passport_no = models.CharField(max_length=32, blank=True)
    photo = models.ImageField(upload_to='customer_photo')

    def __str__(self):
        return self.user.username
