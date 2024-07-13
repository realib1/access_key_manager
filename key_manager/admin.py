from django.contrib import admin
from .models import AccessKey


# Register your models here.
@admin.action(description='Revoke selected keys')
def revoke_keys(modeladmin, request, queryset):
    queryset.update(status='revoked')


class AccessKeyAdmin(admin.ModelAdmin):
    list_display = ('user', 'key', 'status', 'procurement_date', 'expiry_date')
    actions = [revoke_keys]


admin.site.register(AccessKey, AccessKeyAdmin)

