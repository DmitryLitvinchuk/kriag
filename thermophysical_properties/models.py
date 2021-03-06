from django.db import models
from django.contrib.auth.models import User
from substances.models import *


#x. Таблицы теплофизических свойств криопродуктов

# Теплофизические свойства азота на пограничных кривых двухфазной области "жидкость-пар"

#Таблица x.1 Свойства жидкого вещества на линии кипения (по температурам)
# Properties of liquid substance on the boiling line (by temperature)
class PLSBL_T(models.Model):
    # Вещество
    substance = models.ForeignKey(Substance, on_delete=models.CASCADE)
    # T - Температура, К
    temperature = models.DecimalField(max_digits=30, decimal_places=1)
    # P - Давление, МПа
    pressure = models.DecimalField(max_digits=30, decimal_places=3)
    # p' - Плотность, кг/м^3
    density = models.DecimalField(max_digits=30, decimal_places=1)
    # h' - Энтальпия, кДж/кг
    enthalpy = models.DecimalField(max_digits=30, decimal_places=1)
    # r' - Теплота испарения при температуре кипения (Heat of evaporation at boiling point), кДж/кг
    HEBP = models.DecimalField(max_digits=30, decimal_places=1)
    # s' - Энтропия, кДж/(кг*К)
    entropy = models.DecimalField(max_digits=30, decimal_places=3)
    # μ' - Динамическая вязкость, Па*с*10^7 (Dynamic viscosity)
    DV = models.DecimalField(max_digits=30, decimal_places=1)
    # λ' - Теплопроводность, мВт/(м*К) (Thermal conductivity)
    TC = models.DecimalField(max_digits=30, decimal_places=1)

    def __str__(self):
        return "%s %s %s" % (self.substance.name, self.temperature, self.pressure)

    class Meta:
        verbose_name = 'Свойства жидкого вещества на линии кипения (по температурам)'
        verbose_name_plural = 'Свойства жидких веществ на линии кипения (по температурам)'

#Таблица x.2 Свойства парообразного вещества на линии конденсации (по температурам)
# The properties of the vaporous substance on the condensation line (in terms of temperatures)
class PVSCL_T(models.Model):
    # Вещество
    substance = models.ForeignKey(Substance, on_delete=models.CASCADE)
    # T - Температура, К
    temperature = models.DecimalField(max_digits=30, decimal_places=1)
    # P - Давление, МПа
    pressure = models.DecimalField(max_digits=30, decimal_places=3)
    # p'' - Плотность, кг/м^3
    density = models.DecimalField(max_digits=30, decimal_places=1)
    # h'' - Энтальпия, кДж/кг
    enthalpy = models.DecimalField(max_digits=30, decimal_places=1)
    # s'' - Энтропия, кДж/(кг*К)
    entropy = models.DecimalField(max_digits=30, decimal_places=3)
    # μ'' - Динамическая вязкость, Па*с*10^7 (Dynamic viscosity)
    DV = models.DecimalField(max_digits=30, decimal_places=1)
    # λ'' - Теплопроводность, мВт/(м*К) (Thermal conductivity)
    TC = models.DecimalField(max_digits=30, decimal_places=1)

    def __str__(self):
        return "%s %s %s" % (self.substance.name, self.temperature, self.pressure)

    class Meta:
        verbose_name = 'Свойства жидкого вещества на линии конденсации (по температурам)'
        verbose_name_plural = 'Свойства жидких веществ на линии конденсации (по температурам)'

#Таблица x.3 Свойства парообразного вещества на линии кипения (по давлениям)
# Properties of the vaporous substance on the boiling line (on pressures)
class PLSBL_P(models.Model):
    # Вещество
    substance = models.ForeignKey(Substance, on_delete=models.CASCADE)
    # T - Температура, К
    temperature = models.DecimalField(max_digits=30, decimal_places=1)
    # P - Давление, МПа
    pressure = models.DecimalField(max_digits=30, decimal_places=3)
    # p' - Плотность, кг/м^3
    density = models.DecimalField(max_digits=30, decimal_places=1)
    # h' - Энтальпия, кДж/кг
    enthalpy = models.DecimalField(max_digits=30, decimal_places=1)
    # r' - Теплота испарения при температуре кипения (Heat of evaporation at boiling point), кДж/кг
    HEBP = models.DecimalField(max_digits=30, decimal_places=1)
    # s' - Энтропия, кДж/(кг*К)
    entropy = models.DecimalField(max_digits=30, decimal_places=3)
    # μ' - Динамическая вязкость, Па*с*10^7 (Dynamic viscosity)
    DV = models.DecimalField(max_digits=30, decimal_places=1)
    # λ' - Теплопроводность, мВт/(м*К) (Thermal conductivity)
    TC = models.DecimalField(max_digits=30, decimal_places=1)

    def __str__(self):
        return "%s %s %s" % (self.substance.name, self.temperature, self.pressure)

    class Meta:
        verbose_name = 'Свойства жидкого вещества на линии кипения (по давлениям)'
        verbose_name_plural = 'Свойства жидких веществ на линии кипения (по давлениям)'

#Таблица x.4 Свойства парообразного вещества на линии конденсации (по давлениям)
# The properties of the vaporous substance on the condensation line (in terms of pressures)
class PVSCL_P(models.Model):
    # Вещество
    substance = models.ForeignKey(Substance, on_delete=models.CASCADE)
    # T - Температура, К
    temperature = models.DecimalField(max_digits=30, decimal_places=1)
    # P - Давление, МПа
    pressure = models.DecimalField(max_digits=30, decimal_places=3)
    # p'' - Плотность, кг/м^3
    density = models.DecimalField(max_digits=30, decimal_places=1)
    # h'' - Энтальпия, кДж/кг
    enthalpy = models.DecimalField(max_digits=30, decimal_places=1)
    # s'' - Энтропия, кДж/(кг*К)
    entropy = models.DecimalField(max_digits=30, decimal_places=3)
    # μ'' - Динамическая вязкость, Па*с*10^7 (Dynamic viscosity)
    DV = models.DecimalField(max_digits=30, decimal_places=1)
    # λ'' - Теплопроводность, мВт/(м*К) (Thermal conductivity)
    TC = models.DecimalField(max_digits=30, decimal_places=1)

    def __str__(self):
        return "%s %s %s" % (self.substance.name, self.temperature, self.pressure)

    class Meta:
        verbose_name = 'Свойства жидкого вещества на линии конденсации (по давлениям)'
        verbose_name_plural = 'Свойства жидких веществ на линии конденсации (по давлениям)'

#Таблица x.5 Теплофизические свойства веществ в однофазной области
# Термодинамические и переносные свойства веществ в однофазной области
# Thermodynamic, portable properties, single-phase region
class TPPSPR(models.Model):
    # Вещество
    substance = models.ForeignKey(Substance, on_delete=models.CASCADE)
    # T - Температура, К
    temperature = models.DecimalField(max_digits=30, decimal_places=1)
    # P - Давление, МПа
    pressure = models.DecimalField(max_digits=30, decimal_places=2)
    # p - Плотность, кг/м^3
    density = models.DecimalField(max_digits=30, decimal_places=3)
    # h - Энтальпия, кДж/кг
    enthalpy = models.DecimalField(max_digits=30, decimal_places=2)
    # s - Энтропия, кДж/(кг*К)
    entropy = models.DecimalField(max_digits=30, decimal_places=3)
    # μ - Динамическая вязкость, Па*с*10^7 (Dynamic viscosity)
    DV = models.DecimalField(max_digits=30, decimal_places=2)
    # λ - Теплопроводность, мВт/(м*К) (Thermal conductivity)
    TC = models.DecimalField(max_digits=30, decimal_places=2)
    # Cp - Изобарная теплоемкость, кДж/(кг*К) (Isobaric heat capacity)
    IbHC = models.DecimalField(max_digits=30, decimal_places=3)
    # Cv - Изохорная теплоемкость, кДж/(кг*К) (Isochonic heat capacity)
    IhHC = models.DecimalField(max_digits=30, decimal_places=3)
    # Pr - Критерий Прандтля (Criterion of Prandtl)
    CP = models.DecimalField(max_digits=30, decimal_places=3)

    def __str__(self):
        return "%s %s %s" % (self.substance.name, self.temperature, self.pressure)

    class Meta:
        verbose_name = 'Теплофизические свойства вещества в однофазной области'
        verbose_name_plural = 'Теплофизические свойства веществ в однофазной области'
