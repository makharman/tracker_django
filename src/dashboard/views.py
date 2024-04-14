from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from tracker.models import Expense, Income,ExpenseCategory,IncomeCategory
from .forms import ExpenseForm, IncomeForm

def home(request):
    return render(request, 'dashboard/dashboard.html')

class ExpensesListView(ListView):
    model = Expense
    template_name = 'dashboard/expenses.html'
    context_object_name = 'page_obj'
    paginate_by = 8

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)


class ExpensesCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'dashboard/expensesadd.html'
    success_url = reverse_lazy('dashboard:expenses')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, "New Record Added Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ExpenseCategory.objects.all()
        return context

class ExpensesUpdateView(LoginRequiredMixin, UpdateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'dashboard/expensesadd.html'
    success_url = reverse_lazy('dashboard:expenses')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, "Edited Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        context['category'] = ExpenseCategory.objects.all()
        return context

class ExpensesDeleteView(LoginRequiredMixin, DeleteView):
    model = Expense
    success_url = reverse_lazy('dashboard:expenses')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Deleted Successfully")
        return super().delete(request, *args, **kwargs)
    

class IncomeListView(ListView):
    model = Income
    template_name = 'dashboard/income.html'
    context_object_name = 'page_obj_2'
    paginate_by = 5

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)
    
    

class IncomeCreateView(LoginRequiredMixin, CreateView):
    model = Income
    form_class = IncomeForm
    template_name = 'dashboard/incomeadd.html'
    success_url = reverse_lazy('dashboard:income')
    
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, "New Record Added Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = IncomeCategory.objects.all()
        return context


class IncomeUpdateView(LoginRequiredMixin, UpdateView):
    model = Income
    form_class = IncomeForm
    template_name = 'dashboard/incomeadd.html'
    success_url = reverse_lazy('dashboard:income')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, "Edited Successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        context['category'] = IncomeCategory.objects.all()
        return context


class IncomeDeleteView(LoginRequiredMixin, DeleteView):
    model = Expense
    success_url = reverse_lazy('dashboard:income')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Deleted Successfully")
        return super().delete(request, *args, **kwargs)










