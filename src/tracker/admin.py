from django.contrib import admin
from .models import ExpenseCategory, Expense, IncomeCategory, Income

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

