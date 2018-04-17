from django.contrib import admin
from .models import *

# Отображение таблицей в админке
class SubstanceAdmin(admin.ModelAdmin):
	# Отображать все поля, которые есть
	list_display=[field.name for field in Substance._meta.fields]
	# Исключить редактирование поля
	exclude = ['id']


# Модель вещество и подмодель для администрирования
admin.site.register(Substance, SubstanceAdmin)