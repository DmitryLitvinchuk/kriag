from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from substances.models import *
# from django.db.models.signals import post_save
# from django.dispatch import receiver


#Таблицы физических свойств криопродуктов


#Таблица 1.1 Усредненный состав сухого воздуха [31]
class ACDA(models.Model):
    #Компонент
    component = models.ForeignKey(Substance, on_delete=models.CASCADE)
    #Объемная доля компонента в воздухе, %
    cvf = models.CharField(max_length=100)
    #Массовая доля компонента в воздухе, %
    cmf = models.CharField(max_length=100)

    def __str__(self):
        return "%s %s %s" % (self.component.name, self.cvf, self.cmf)

    class Meta:
        verbose_name = 'Компонент усредненного состава сухого воздуха'
        verbose_name_plural = 'Компоненты усредненного состава сухого воздуха'


#Таблица 1.2 Значение влагосодержания воздуха при p=99325 Па
#            в зависимости от температуры для φ=1,0 [2]
#            The moisture content of air as a function of temperature
class MCAFT(models.Model):
    # Температура
    temperature = models.CharField(max_length=100)
    # Влагосодержание, d*10^4 кг H2O/кг воздуха
    moisture = models.CharField(max_length=100)

    def __str__(self):
        return "%s %s" % (self.temperature, self.moisture)

    class Meta:
        verbose_name = 'Значение влагосодержания воздуха'
        verbose_name_plural = 'Значения влагосодержания воздуха'


#Таблица 1.3 Значение влагосодержания в различных криопродуктов
#            в зависимости от давления и температуры [2]
# Value of moisture content in various cryogenic products depending on pressure and temperature [2]
class MCC_PT(models.Model):
    #Компонент
    component = models.ForeignKey(Substance, on_delete=models.CASCADE)
    # Температура
    temperature = models.CharField(max_length=100)
    # Давление
    pressure = models.CharField(max_length=100)
    # Влагосодержание, d*10^4 кг H2O/кг воздуха
    moisture = models.CharField(max_length=100)

    def __str__(self):
        return "%s %s" % (self.component.name, self.temperature)

    class Meta:
        verbose_name = 'Значение влагосодержания криопродукта'
        verbose_name_plural = 'Значения влагосодержания криопродуктов'