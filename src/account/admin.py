from django.contrib import admin
from account.models import User

@admin.register(User)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'password', 'first_name', 'last_name', 'date_of_birth', 'mobile_phone', 'gender', 'is_active', 'created_at', 'updated_at')
    
    
    readonly_fields = (
        'created_at',
        'updated_at',
        'password',
    )

