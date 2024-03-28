from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Expense, Income

# class HomeView(TemplateView):
#     template_name = 'tracker/tracker.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
        
#         expenses = Expense.objects.all()
#         incomes = Income.objects.all()
        
#         context['expenses'] = expenses
#         context['incomes'] = incomes

#         return context
