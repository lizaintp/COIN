from django.db import models

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# Create your models here.
phone_regex = RegexValidator(regex=r'\+996\d{9}$', message='Телефон должен начинаться с +996')

class User(AbstractUser):
    phone = models.PositiveIntegerField(
        max_length=255, 
        verbose_name='Телефон'

    )
    age = models.IntegerField(
        verbose_name='Возраст',
        null=True,
        blank=True
    )
    direction = models.CharField(
        max_length=255,
        verbose_name='Направление'
    )
    balance = models.PositiveIntegerField(
        verbose_name='Баланс',
        default=4
    )
    wallet  = models.IntegerField(
        verbose_name='Кошелек',
        default=0,
        blank=True, null=True
    )

    def __str__(self):
        return f'{self.username}-{self.balance}'
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'