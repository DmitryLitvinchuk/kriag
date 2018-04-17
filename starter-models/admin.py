from django.contrib import admin
from .models import *

# class SubstanceAdmin(admin.ModelAdmin):
# 	list_display=[field.name for field in Substance._meta.fields]
# 	exclude = ['id']


# admin.site.register(Post)
# admin.site.register(ACDA)
# admin.site.register(Profile)
# admin.site.register(Substance, SubstanceAdmin)