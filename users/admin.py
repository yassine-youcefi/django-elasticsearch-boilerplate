from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User, UserConfirmation, UserSocialLinks

ADDITIONAL_USER_FIELDS = (
    ("Account Confirmation", {
     'fields': ('picture', 'about', 'phone_number', 'is_confirmed', 'gender', 'date_of_birth')
     }),
)


class MyUserAdmin(UserAdmin):
    model = User
    add_fieldsets = UserAdmin.add_fieldsets + ADDITIONAL_USER_FIELDS
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_USER_FIELDS
    list_display = ('username', 'email', 'phone_number',
                    'first_name', 'last_name', 'is_confirmed')


admin.site.register(User, MyUserAdmin)


@admin.register(UserConfirmation)
class UserConfirmationAdmin(admin.ModelAdmin):
    list_display = ['user', 'confirmation_code', 'email_confirmed']
    search_fields = ['user__username']
    raw_id_fields = ['user']


@admin.register(UserSocialLinks)
class UserSocialLinksAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    search_fields = ['user__username']