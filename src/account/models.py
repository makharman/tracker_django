from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

class User(AbstractUser):
    CURRENSY_CHOICES = (
        ("TENGE", "₸"),
        ("DOLLAR", "$"),
        ("RUBL", "₽"),
    )

    currency = models.CharField(max_length=6,
        choices=CURRENSY_CHOICES,
        default="TENGE")

    username = None
    email = models.EmailField("email address", unique=True)
    # user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)
    mobile_phone = models.CharField(max_length=15, null=True, blank=True)
    
    GENDER_CHOICES = (
    (1, 'Male'),
    (2, 'Female'),
    )
    
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        auto_now_add=True,null=True
    )
    updated_at = models.DateTimeField(
        auto_now=True, null=True
    )
    
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    class Meta:
        db_table='UserAccount'
        ordering = ['-created_at']
        verbose_name = 'UserAccount'
        verbose_name_plural = 'UserAccounts'

    def __str__(self) -> str:
        return f'{self.id} - {self.email}' 
    
    