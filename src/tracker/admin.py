from django.contrib import admin
from .models import AccountProfile, UserProfile, ExpenseCategory, Expense, IncomeCategory, Income


@admin.register(AccountProfile)
class AccountProfileAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'email', 'password')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'date_of_birth', 'address', 'phone_number', 'gender', 'is_active')

@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('spent_amount', 'description', 'category', 'date', 'user')

@admin.register(IncomeCategory)
class IncomeCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('earned_amount', 'description', 'category', 'date', 'user')
