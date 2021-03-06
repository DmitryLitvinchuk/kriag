from django.contrib import admin
from .models import *

class SubstanceTPPSPR(admin.ModelAdmin):
	list_display=[field.name for field in TPPSPR._meta.fields]
	exclude = ['id']

class SubstancePLSBL_T(admin.ModelAdmin):
	list_display=[field.name for field in PLSBL_T._meta.fields]
	exclude = ['id']

class SubstancePVSCL_T(admin.ModelAdmin):
	list_display=[field.name for field in PVSCL_T._meta.fields]
	exclude = ['id']

class SubstancePLSBL_P(admin.ModelAdmin):
	list_display=[field.name for field in PLSBL_P._meta.fields]
	exclude = ['id']

class SubstancePVSCL_P(admin.ModelAdmin):
	list_display=[field.name for field in PVSCL_P._meta.fields]
	exclude = ['id']
	
admin.site.register(PLSBL_T, SubstancePLSBL_T)
admin.site.register(PVSCL_T, SubstancePVSCL_T)
admin.site.register(PLSBL_P, SubstancePLSBL_P)
admin.site.register(PVSCL_P, SubstancePVSCL_P)
admin.site.register(TPPSPR, SubstanceTPPSPR)
