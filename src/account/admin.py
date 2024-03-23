from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'date_of_birth', 'mobile_phone', 'gender', 'is_active','created_at', 'updated_at')
    readonly_fields = (
        'created_at',
        'updated_at',
    )
