from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    model = CustomUser
    list_display = ('username', 'is_staff')
    search_fields = ('username', 'email')
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(CustomUser, CustomUserAdmin)
