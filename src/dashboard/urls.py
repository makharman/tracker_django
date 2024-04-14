from django.urls import path
from . import views
from .views import home
from .views import ExpensesListView, ExpensesCreateView, ExpensesUpdateView, ExpensesDeleteView,IncomeListView, IncomeCreateView, IncomeUpdateView, IncomeDeleteView
app_name = 'dashboard'


urlpatterns = [
    path('home/', home, name='home'),  
    path('expenses/', ExpensesListView.as_view(), name='expenses'), 
    path('expenses/add/', ExpensesCreateView.as_view(), name='add'),
    path('expenses/edit/<int:pk>',ExpensesUpdateView.as_view(), name='edit'),
    path('expenses/delete/<int:pk>',ExpensesDeleteView.as_view(), name='delete'),   
    path('income/', IncomeListView.as_view(), name='income'), 
    path('income/add/', IncomeCreateView.as_view(), name='incomeadd'),
    path('income/edit/<int:pk>',IncomeUpdateView.as_view(), name='incomeedit'),
    path('income/delete/<int:pk>',IncomeDeleteView.as_view(), name='incomedelete'),
]


