from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import CustomUserChangeForm, CustomUserCreationForm
from django.utils.translation import ugettext_lazy as _
from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference the removed 'username' field
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name',
                                         'phone_number', 'mobile_number',
                                         'zip_code', 'home_address',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('email', 'first_name', 'last_name',
                    'mobile_number', 'phone_number',
                    'is_staff')
    search_fields = ('email', 'first_name', 'last_name', 'mobile_number', 'phone_number')
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
