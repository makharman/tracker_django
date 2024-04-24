from django.urls import path
from .views import (
    ExpenseListModel,
    IncomeListModel,
    ExpenseAddModel,
    IncomeAddModel,
    ExpenseEditModel,
    IncomeEditModel,
    ExpenseDeleteModel,
    IncomeDeleteModel,
    AccountApi,
    AccountDetailApi
)

urlpatterns = [
    
    path('account/', AccountApi.as_view(), name="account"),
    path('account/<int:pk>/', AccountDetailApi.as_view(), name="account_detail"),
    
    
    path('expenses/', ExpenseListModel.as_view(), name='expense-list'),
    path('incomes/', IncomeListModel.as_view(), name='income-list'),

    path('expenses/add/', ExpenseAddModel.as_view(), name='expense-create'),
    path('incomes/add/', IncomeAddModel.as_view(), name='income-create'),

    path('expenses/<int:pk>/edit/', ExpenseEditModel.as_view(), name='expense-detail-update'),
    path('incomes/<int:pk>/edit/', IncomeEditModel.as_view(), name='income-detail-update'),
    path('expenses/<int:pk>/delete/', ExpenseDeleteModel.as_view(), name='expense-delete'),
    path('incomes/<int:pk>/delete/', IncomeDeleteModel.as_view(), name='income-delete'),
]
