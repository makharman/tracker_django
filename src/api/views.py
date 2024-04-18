from rest_framework.generics import CreateAPIView,ListAPIView, RetrieveUpdateAPIView
from tracker.models import Expense, Income
from .serializers import ExpenseSerializer, IncomeSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

class ExpenseListModel(ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 

class IncomeListModel(ListAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 


class ExpenseAddModel(CreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated] 
    

class IncomeAddModel(CreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated] 
    
    
class ExpenseEditModel(RetrieveUpdateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated] 

class IncomeEditModel(RetrieveUpdateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated] 
    
class ExpenseDeleteModel(RetrieveUpdateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAdminUser] 
    

class IncomeDeleteModel(RetrieveUpdateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsAdminUser] 
    
       
