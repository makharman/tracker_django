from rest_framework.generics import CreateAPIView,ListAPIView, RetrieveUpdateAPIView
from tracker.models import Expense, Income
from .serializers import ExpenseSerializer, IncomeSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

class ExpenseListModelSerializer(ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 

class IncomeListModelSerializer(ListAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 
    
    


class ExpenseAddModelSerializer(CreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated] 
    

class IncomeAddModelSerializer(CreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated] 
    
    
class ExpenseEditModelSerializer(RetrieveUpdateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated] 

class IncomeEditModelSerializer(RetrieveUpdateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated] 
    
class ExpenseDeleteModelSerializer(RetrieveUpdateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAdminUser] 
    

class IncomeDeleteModelSerializer(RetrieveUpdateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsAdminUser] 
    
       
