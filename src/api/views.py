from rest_framework.generics import CreateAPIView,ListAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework import generics
from tracker.models import Expense, Income
from .serializers import ExpenseSerializer, IncomeSerializer,RegisterSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import permissions, response
from account.models import User
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework import filters
import requests
from django.views.generic import View
from django.http import JsonResponse




class AccountApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
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
        
    def get(self, request, *args,  **kwargs):
        users = User.object.all()
        user_data = UserSerializer(users, many=True)
        return response.Response(user_data.data)



class UserListAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class AccountDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_queryset(self):
        print(self.request)
        return super().get_queryset()

class ExpenseListModel(ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated] 
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ["category"]
    search_fields = ["description"]
    ordering_fields = ["spent_amount"]

class IncomeListModel(ListAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [permissions.IsAuthenticated] 
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ["category"]
    search_fields = ["description"]
    ordering_fields = ["earned_amount"]
    
    


class ExpenseAddModel(CreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated] 

      

class IncomeAddModel(CreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [permissions.IsAuthenticated,] 
    
    
    
    
class ExpenseEditModel(RetrieveUpdateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated,] 

class IncomeEditModel(RetrieveUpdateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [permissions.IsAuthenticated,] 
    
class ExpenseDeleteModel(RetrieveDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated ] 
    
    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        message = "Expense has been deleted sucsesfully"
        return response.Response({
            "message": message
        })
    

class IncomeDeleteModel(RetrieveDestroyAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [permissions.IsAuthenticated] 
    
       
class ExchangeRateAPIView(View):
    def get(self, request, *args, **kwargs):
        url = "https://exchange-rates.abstractapi.com/v1/live"
        querystring = {"api_key":"0d517f2e89654646994dd84fc2099462","base":"CZK"}

        
        response = requests.request("GET", url, params=querystring)
        exchange_data = response.json()
        
        return JsonResponse(exchange_data)