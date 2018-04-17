from django.contrib import admin
from .models import *

class ACDAAdmin(admin.ModelAdmin):
	list_display=[field.name for field in ACDA._meta.fields]

admin.site.register(ACDA, ACDAAdmin)
