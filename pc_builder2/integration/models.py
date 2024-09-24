from django.db import models
# Create your models here.


class BaseGPU(models.Model):
    """Видеокарта"""

    short_name = models.CharField(max_length=100,verbose_name="Сокращенное название")
    perfomance_index = models.FloatField()
    tdp = models.IntegerField()


class BaseCPU(models.Model):
    """Процессор"""

    name = models.CharField(max_length=100)
    perfomance_index = models.FloatField()
    socket = models.IntegerField()
    is_graphics = models.BooleanField()


class BaseMotherBoard(models.Model):
    """Материнская плата"""

    name = models.CharField(max_length=100)
    cost = models.FloatField()
    socket = models.IntegerField()
    power_phases = models.IntegerField()
    type_of_memory = models.CharField(max_length=100)
    chipset = models.CharField(max_length=100)


class BaseRAM(models.Model):
    """Оперативная память"""

    name = models.CharField(max_length=100)
    value_gb = models.IntegerField()
    type = models.CharField(max_length=100)
    frequency = models.IntegerField(null=True)
    is_game = models.BooleanField()
    count = models.IntegerField()


class BasePowerUnit(models.Model):
    """Блок питания"""

    name = models.CharField(max_length=100)
    power = models.IntegerField()

class DNSCPU(models.Model):
    """Процессор от dns"""
    base = models.ForeignKey(BaseCPU, on_delete=models.CASCADE)


class DNSGPU(models.Model):
    """Видеокарта от dns"""
    base = models.ForeignKey(BaseGPU, on_delete=models.CASCADE)
