from django.urls import path, include
from account import views

urlpatterns = [
   
    # api
    path('register/', views.RegisterApi.as_view(), name="register")
]
