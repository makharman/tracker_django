from rest_framework.generics import CreateAPIView,ListAPIView, RetrieveUpdateAPIView
from tracker.models import Expense, Income
from .serializers import ExpenseSerializer, IncomeSerializer

class ExpenseListModelSerializer(ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class IncomeListModelSerializer(ListAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class ExpenseAddModelSerializer(CreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class IncomeAddModelSerializer(CreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    
class ExpenseEditModelSerializer(RetrieveUpdateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class IncomeEditModelSerializer(RetrieveUpdateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    
class ExpenseDeleteModelSerializer(RetrieveUpdateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class IncomeDeleteModelSerializer(RetrieveUpdateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
       
