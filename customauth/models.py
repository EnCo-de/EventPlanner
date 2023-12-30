from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator, MinLengthValidator, RegexValidator

# Create your models here.
class ClientUserModel(AbstractUser):
    email = models.EmailField(
        verbose_name="Էլ.փոստի հասցե",
        max_length=255,
        unique=True,
    )
    mobile = models.CharField(max_length=15, unique=True, validators=[
        MinLengthValidator(9),
        RegexValidator(r'[0-9]$'),
        ])
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'mobile']

    def __str__(self):
        return self.email