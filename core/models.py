from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    code = models.IntegerField(default=0)
    code_time_create = models.IntegerField(default=0)

    def __str__(self):
        return self.username
    
    @property
    def balance_as_int(self):
        return int(self.balance)
    

class ServerConfig(models.Model):
    name = models.CharField(max_length=100)  # Название сервера (например, V-01)
    proc = models.CharField(max_length=100)  # Процессор
    memory = models.CharField(max_length=100)  # Оперативная память
    nvme = models.CharField(max_length=100)  # Место на диске
    internet = models.CharField(max_length=100)  # Скорость интернета
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    location = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class GeoBlock(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='geo_images/')
    config_id = models.IntegerField(unique=True)
    location = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    