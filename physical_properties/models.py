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
    substance = models.ForeignKey(Substance, on_delete=models.CASCADE)
    #Объемная доля компонента в воздухе, %
    cvf = models.CharField(max_length=100)
    #Массовая доля компонента в воздухе, %
    cmf = models.CharField(max_length=100)

    def __str__(self):
        return "%s %s %s" % (self.substance.name, self.cvf, self.cmf)

    class Meta:
        verbose_name = 'Усредненный состав воздуха'
        verbose_name_plural = 'Усредненный состав воздуха'


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
    substance = models.ForeignKey(Substance, on_delete=models.CASCADE)
    # Температура
    temperature = models.CharField(max_length=100)
    # Давление
    pressure = models.CharField(max_length=100)
    # Влагосодержание, d*10^4 кг H2O/кг воздуха
    moisture = models.CharField(max_length=100)

    def __str__(self):
        return "%s %s" % (self.substance.name, self.temperature)

    class Meta:
        verbose_name = 'Значение влагосодержания криопродукта'
        verbose_name_plural = 'Значения влагосодержания криопродуктов'

#Таблица 1.5 Значения основных физических констант газов
# The values of the basic physical constants of gases
class BPCG(models.Model):
    #Компонент
    substance = models.ForeignKey(Substance, on_delete=models.CASCADE)
    # Атомная или молекулярная масса M кг/моль
    molecular_mass = models.CharField(max_length=100)
    # Плотность при 273К и p=pн, кг/м^3
    density = models.CharField(max_length=100)
    # Газовая постоянная R, Дж/(кг*К)
    gas_constant = models.CharField(max_length=100)
    # Критическая температура, К
    critical_temperature = models.CharField(max_length=100)
    # Критическое давление, МПа
    critical_pressure = models.CharField(max_length=100)
    # Критическая плотность, кг/м^3
    critical_density = models.CharField(max_length=100)
    # Температура тройной точки, К
    triple_point_temperature = models.CharField(max_length=100)
    # Теплота испарения при нормальной температуре кипения, кДж/кг
    evaporation_heat = models.CharField(max_length=100)
    # Теплота плавления, кДж/кг
    fusion_heat = models.CharField(max_length=100)
    # Температура кипения при p=pн, К
    boiling_temperature = models.CharField(max_length=100)
    # Плотность жидкости при нормальной температуре кипения, кг/м^3
    fluid_density = models.CharField(max_length=100)
    # Теплоемкость при p=pн b 273К Cp, кДж/(кг*К)
    heat_capacity_cp = models.CharField(max_length=100)
    # Теплоемкость при p=pн b 273К Cv, кДж/(кг*К)
    heat_capacity_cv = models.CharField(max_length=100)

    def __str__(self):
        return "%s %s" % (self.substance.id, self.substance.chemical_formula)

    class Meta:
        verbose_name = 'Значение основных физических констант газов'
        verbose_name_plural = 'Значения основных физических констант газов'