from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
from thermophysical_properties.models import *
from physical_properties.models import *
from decimal import Decimal
# from django.views.generic.edit import FormView
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.http import HttpResponseRedirect
# from django.views.generic.base import View
# from django.contrib.auth import logout, login
# from django.contrib.auth.decorators import login_required
# from django.db import transaction
# from django import forms
# from django.contrib import messages
# from .forms import *

# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/post_list.html', {'posts': posts})

"""
Отображение таблицы с веществами
"""
def substances_table(request):
    substances = Substance.objects.all()
    return render(request, 'substances/substances_table.html', {'substances': substances})


def dashboard_substance(request, substance_id):
    substance = Substance.objects.get(pk=substance_id)
    BPCGs = BPCG.objects.filter(substance=substance_id)
    #Таблица x.5 Теплофоизические и переносные свойства веществ в однофазной области
    pressure = '0.10'
    TPPSPRs = TPPSPR.objects.filter(substance=substance_id, pressure=pressure)
    p = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9,
    1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0,
    12.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
    TPPSPR_title = 'Теплофоизические и переносные свойства '+substance.name+'а'+' в однофазной области при 0,1 МПа'
    #Таблица x.1 Свойства жидкого вещества на линии кипения (по температурам)
    PLSBL_Ts = PLSBL_T.objects.filter(substance=substance_id)
    PLSBL_T_title = 'Свойства жидкого '+substance.name+'а'+' линии кипения (по температурам)'
    #Таблица x.2 Свойства парообразного вещества на линии конденсации (по температурам)
    PVSCL_Ts = PVSCL_T.objects.filter(substance=substance_id)
    PVSCL_T_title = 'Свойства парообразного вещества на линии конденсации (по температурам)'
    #Таблица x.3 Свойства парообразного вещества на линии кипения (по давлениям)
    PLSBL_Ps = PLSBL_P.objects.filter(substance=substance_id)
    PLSBL_P_title = 'Свойства парообразного вещества на линии кипения (по давлениям)'
    #Таблица x.4 Свойства парообразного вещества на линии конденсации (по давлениям)
    PVSCL_Ps = PVSCL_P.objects.filter(substance=substance_id)
    PVSCL_P_title = 'Свойства парообразного вещества на линии конденсации (по давлениям)'
    return render(request, 'substances/dashboard-substance.html', locals())
