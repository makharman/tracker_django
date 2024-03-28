
from django.db import models
from django.contrib.auth.models import User


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    

class Expense(models.Model):
    spent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    date = models.DateField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)


  
class IncomeCategory(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    

class Income(models.Model):
    earned_amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)
    date = models.DateField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
