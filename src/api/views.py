from rest_framework.generics import CreateAPIView,ListAPIView, RetrieveUpdateAPIView
from rest_framework import generics
from tracker.models import Expense, Income
from .serializers import ExpenseSerializer, IncomeSerializer,RegisterSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user_data = UserSerializer(
            user, context=self.get_serializer_context()
        )
        
        user = user_data.data
        return Response(
            {
            "user": user,
            "message": "User Created Successfully.  Now perform Login to get your token",
            }
        )

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
    
       
