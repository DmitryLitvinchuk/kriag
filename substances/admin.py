from django.contrib import admin
from .models import *

# Отображение таблицей в админке
class SubstanceAdmin(admin.ModelAdmin):
	# Отображать все поля, которые есть
	list_display=[field.name for field in Substance._meta.fields]
	# Исключить редактирование поля
	exclude = ['id']

# Отображение таблицей в админке
class InfoAdmin(admin.ModelAdmin):
	# Отображать все поля, которые есть
	list_display=[field.name for field in Info._meta.fields]
	# Исключить редактирование поля
	exclude = ['id']


# Модель вещество и подмодель для администрирования
admin.site.register(Substance, SubstanceAdmin)

# Модель вещество и подмодель для администрирования
admin.site.register(Info, InfoAdmin)