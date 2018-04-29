from django.contrib import admin
from .models import *

class ACDAAdmin(admin.ModelAdmin):
	list_display=[field.name for field in ACDA._meta.fields]

class MCAFTAdmin(admin.ModelAdmin):
	list_display=[field.name for field in MCAFT._meta.fields]

class MCC_PTAdmin(admin.ModelAdmin):
	list_display=[field.name for field in MCC_PT._meta.fields]

class BPCGAdmin(admin.ModelAdmin):
	list_display=[field.name for field in BPCG._meta.fields]

admin.site.register(ACDA, ACDAAdmin)
admin.site.register(MCAFT, MCAFTAdmin)
admin.site.register(MCC_PT, MCC_PTAdmin)
admin.site.register(BPCG, BPCGAdmin)