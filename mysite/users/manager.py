from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import Permission, Group
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, phone, password=None, company=False):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=CustomUserManager.normalize_email(email), phone=phone, )
        user.set_password(password)
        user.save(using=self._db)

        # add to user group and set permissions
        if company:
            g = Group.objects.get(name='company')
            p = Permission.objects.get(codename='add_company')
        else:
            g = Group.objects.get(name='user')
            p = Permission.objects.get(codename='add_user')
        g.user_set.add(user)
        user.user_permissions.add(p)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)