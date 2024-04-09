from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    CURRENSY_CHOICES = (
        ("TENGE", "₸"),
        ("DOLLAR", "$"),
        ("RUBL", "₽"),
    )

    currency = models.CharField(max_length=6,
        choices=CURRENSY_CHOICES,
        default="TENGE")

    
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    mobile_phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,null=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата обновления',
        auto_now=True, null=True
    )
    
    class Meta:
        db_table='UserAccount'
        ordering = ['-created_at']
        verbose_name = 'UserAccount'
        verbose_name_plural = 'UserAccounts '

    def __str__(self) -> str:
        return f'{self.id} - {self.mobile_phone}' 
    
    