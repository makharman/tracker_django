from django.urls import path
from .views import (
    ExpenseListModelSerializer,
    IncomeListModelSerializer,
    ExpenseAddModelSerializer,
    IncomeAddModelSerializer,
    ExpenseEditModelSerializer,
    IncomeEditModelSerializer,
    ExpenseDeleteModelSerializer,
    IncomeDeleteModelSerializer
)

urlpatterns = [
   
    
    path('expenses/', ExpenseListModelSerializer.as_view(), name='expense-list'),
    path('incomes/', IncomeListModelSerializer.as_view(), name='income-list'),

    path('expenses/add/', ExpenseAddModelSerializer.as_view(), name='expense-create'),
    path('incomes/add/', IncomeAddModelSerializer.as_view(), name='income-create'),

    path('expenses/<int:pk>/edit/', ExpenseEditModelSerializer.as_view(), name='expense-detail-update'),
    path('incomes/<int:pk>/edit/', IncomeEditModelSerializer.as_view(), name='income-detail-update'),
    path('expenses/<int:pk>/delete/', ExpenseDeleteModelSerializer.as_view(), name='expense-delete'),
    path('incomes/<int:pk>/delete/', IncomeDeleteModelSerializer.as_view(), name='income-delete'),
]
