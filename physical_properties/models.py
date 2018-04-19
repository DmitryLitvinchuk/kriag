from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from substances.models import *
# from django.db.models.signals import post_save
# from django.dispatch import receiver


#Таблицы физических свойств криопродуктов

#Таблица 1.1
#Усредненный состав сухого воздуха [31]
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
