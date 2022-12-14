from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager
from orders.models import Order


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=35)
    phone = models.CharField(max_length=11)
    orders = models.ManyToManyField(Order, default=None, null=True, blank=True)
    # password1 = models.CharField(max_length=100)
    # password2 = models.CharField(max_length=100)
    address = models.CharField(max_length=300, default=None, null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email