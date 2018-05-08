from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#Вещество
class Substance(models.Model):
    #Название
    name = models.CharField(max_length=30)
    #Химическая формула
    chemical_formula = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return "%s %s" % (self.name, self.chemical_formula)

    class Meta:
        verbose_name = 'Вещество'
        verbose_name_plural = 'Вещества'

#Информация о веществе
class Info(models.Model):
	# Вещество
    substance = models.ForeignKey(Substance, on_delete=models.CASCADE)
    # Название
    title = models.CharField(max_length=30)
    # Описание
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.substance.name, self.title)

    class Meta:
        verbose_name = 'Информация о веществе'
        verbose_name_plural = 'Информация о веществах'