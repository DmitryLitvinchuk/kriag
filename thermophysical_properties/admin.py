from django.contrib import admin
from .models import *

class SubstanceTPPSPR(admin.ModelAdmin):
	list_display=[field.name for field in TPPSPR._meta.fields]
	exclude = ['id']

admin.site.register(TPPSPR, SubstanceTPPSPR)