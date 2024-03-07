
from django.db import models

class AccountProfile(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

class UserProfile(models.Model):
    user = models.OneToOneField(AccountProfile, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=255)

class Expense(models.Model):
    spent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    date = models.DateField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class IncomeCategory(models.Model):
    name = models.CharField(max_length=255)

class Income(models.Model):
    earned_amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)
    date = models.DateField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
  
    
    
