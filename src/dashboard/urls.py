from django.urls import path
from . import views
from .views import home
from .views import ExpensesListView, ExpensesCreateView, ExpensesUpdateView, ExpensesDeleteView,IncomeListView, IncomeCreateView, IncomeUpdateView, IncomeDeleteView
app_name = 'dashboard'


urlpatterns = [
    path('home/', home, name='home'),  
    path('expenses/', ExpensesListView.as_view(), name='expenses'), 
    path('expenses/add/', ExpensesCreateView.as_view(), name='add'),
    path('expenses/edit/<int:id>',ExpensesUpdateView.as_view(), name='edit'),
    path('expenses/delete/<int:id>',ExpensesDeleteView.as_view(), name='delete'),   
    path('income/', IncomeListView.as_view(), name='income'), 
    path('income/add/', IncomeCreateView.as_view(), name='incomeadd'),
    path('income/edit/<int:id>',IncomeUpdateView.as_view(), name='incomeedit'),
    path('income/delete/<int:id>',IncomeDeleteView.as_view(), name='incomedelete'),
]


