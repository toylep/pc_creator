from django.db import models

# Create your models here.


class BaseGPU(models.Model):
    """Видеокарта"""

    short_name = models.CharField(max_length=100,verbose_name="Сокращенное название")
    perfomance_index = models.FloatField(verbose_name="Индекс производительности")
    tdp = models.IntegerField(verbose_name="Пакет тепловыделения")


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


class Category(models.Model):
    """Категория ПК"""

    name = models.CharField(max_length=50)
    cpu = models.FloatField()
    gpu = models.FloatField()
    motherboard = models.FloatField()
    ram = models.FloatField()
    power_unit = models.FloatField()


class Configuration(models.Model):
    """Конфигурация ПК(Сборка)"""

    cpu = models.ForeignKey(BaseCPU, on_delete=models.CASCADE)
    gpu = models.ForeignKey(BaseGPU, on_delete=models.CASCADE, null=True)
    motherboard = models.ForeignKey(BaseMotherBoard, on_delete=models.CASCADE)
    ram = models.ForeignKey(BaseRAM, on_delete=models.CASCADE)
    power_unit = models.ForeignKey(BasePowerUnit, on_delete=models.CASCADE)
