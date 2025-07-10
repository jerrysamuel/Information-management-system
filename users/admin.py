from django.contrib import admin
from users.models import Profile, Account

@admin.action(description="Make selected users admin")
def make_admin(modeladmin, request, queryset):
    queryset.update(is_admin=True, role='admin')

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("email", "is_admin", "is_staff", "is_active")  # adjust fields as needed
    actions = [make_admin]

admin.site.register(Profile)
