from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Car(models.Model):
    vin = models.CharField(verbose_name='vin', db_index=True, unique=True, max_length=64)
    color = models.CharField(verbose_name='color', max_length=64)
    brand = models.CharField(verbose_name='Brand', max_length=64)
    CAR_TYPES = (
        (1, 'sedan'),
        (2, 'hot_hetch'),
    )
    car_type = models.IntegerField(verbose_name='Car_type', choices=CAR_TYPES)
    user = models.ForeignKey(User, verbose_name='USER', on_delete=models.CASCADE)
