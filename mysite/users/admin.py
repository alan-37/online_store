from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ('email','first_name', 'last_name', 'phone', 'is_staff', 'is_active','date_joined', 'is_superuser')
    list_filter = ('email','first_name', 'last_name', 'phone', 'is_staff', 'is_active','date_joined', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password','first_name', 'last_name', 'phone', 'address', 'orders')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'date_joined', 'is_superuser', 'groups' )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'phone', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser', 'groups')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)

# class CustomUserAdmin (admin.ModelAdmin):
#     list_display = [field.name for field in CustomUser._meta.fields]
#
#
#     class Meta:
#         model = CustomUser

# admin.site.register(CustomUser, CustomUserAdmin)