from django.db import models

class Configuration(models.Model):
    """Конфигурация ПК(Сборка)"""

    cpu = models.ForeignKey(BaseCPU, on_delete=models.CASCADE)
    gpu = models.ForeignKey(BaseGPU, on_delete=models.CASCADE, null=True)
    motherboard = models.ForeignKey(BaseMotherBoard, on_delete=models.CASCADE)
    ram = models.ForeignKey(BaseRAM, on_delete=models.CASCADE)
    power_unit = models.ForeignKey(BasePowerUnit, on_delete=models.CASCADE)

class Category(models.Model):
    """Категория ПК"""

    name = models.CharField(max_length=50)
    cpu = models.FloatField()
    gpu = models.FloatField()
    motherboard = models.FloatField()
    ram = models.FloatField()
    power_unit = models.FloatField()