from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
from decimal import Decimal
from django.db.models import Q
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
import math
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

#Таблица x.1 Свойства жидкого вещества на линии кипения (по температурам)
def PLSBL_T_table(request, substance_id):
	# В таблице отбираем значения с substance_id равным переданному значению
    PLSBL_Ts = PLSBL_T.objects.filter(substance=substance_id)
    PLSBL_T_title = 'Свойства жидкого вещества на линии кипения (по температурам)'
    return render(request, 't-prop/plsbl_t.html', locals())

#Таблица x.2 Свойства парообразного вещества на линии конденсации (по температурам)
def PVSCL_T_table(request, substance_id):
	# В таблице отбираем значения с substance_id равным переданному значению
    PVSCL_Ts = PVSCL_T.objects.filter(substance=substance_id)
    PVSCL_T_title = 'Свойства парообразного вещества на линии конденсации (по температурам)'
    return render(request, 't-prop/pvscl_t.html', locals())

#Таблица x.3 Свойства парообразного вещества на линии кипения (по давлениям)
def PLSBL_P_table(request, substance_id):
	# В таблице отбираем значения с substance_id равным переданному значению
    PLSBL_Ps = PLSBL_P.objects.filter(substance=substance_id)
    PLSBL_P_title = 'Свойства парообразного вещества на линии кипения (по давлениям)'
    return render(request, 't-prop/plsbl_p.html', locals())

#Таблица x.4 Свойства парообразного вещества на линии конденсации (по давлениям)
def PVSCL_P_table(request, substance_id):
	# В таблице отбираем значения с substance_id равным переданному значению
    PVSCL_Ps = PVSCL_P.objects.filter(substance=substance_id)
    PVSCL_P_title = 'Свойства парообразного вещества на линии конденсации (по давлениям)'
    return render(request, 't-prop/pvscl_p.html', locals())

#Таблица x.5 Теплофоизические и переносные свойства веществ в однофазной области
def TPPSPR_table(request, substance_id):
	# В таблице отбираем значения с substance_id равным переданному значению
    TPPSPRs = TPPSPR.objects.filter(substance=substance_id)
    substance = Substance.objects.get(pk=substance_id)
    # Все доступные значения давлений
    p = []
    for i in TPPSPRs:
        if float(i.pressure) not in p:
            press = float(i.pressure)
            p.append(press)
    # p = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9,
    # 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0,
    # 12.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
    TPPSPR_title = 'Теплофоизические и переносные свойства '+substance.name+'а'+' в однофазной области'
    return render(request, 't-prop/tppsprs.html', locals())

#Таблица x.5 Теплофоизические и переносные свойства веществ в однофазной области с фильтром
def TPPSPR_table_pressure(request, substance_id, pressure):
    # В таблице отбираем значения с substance_id равным переданному значению
    TPPSPRs = TPPSPR.objects.filter(substance=substance_id)
    # Все доступные значения давлений
    p = []
    for i in TPPSPRs:
        if float(i.pressure) not in p:
            press = float(i.pressure)
            p.append(press)
	# В таблице отбираем значения с substance_id равным переданному значению
    TPPSPRs = TPPSPR.objects.filter(substance=substance_id, pressure=pressure)
    substance = Substance.objects.get(pk=substance_id)
    TPPSPR_title = 'Теплофоизические и переносные свойства '+substance.name+'а'+' в однофазной области при давлении '+pressure+'МПа'
    return render(request, 't-prop/tppsprs.html', locals())

def TPPSPR_in_point_create(request, substance_id):
    substance = Substance.objects.get(pk=substance_id)
    title = 'Расчет теплофизических и переносных свойств для '+substance.name+'а'
    block_header = 'Введите расчетные значения'
    TPPSPRs = TPPSPR.objects.filter(substance=substance_id)
    TPPSPRs_first = TPPSPRs.first()
    TPPSPRs_last = TPPSPRs.last()
    input_1_min = TPPSPRs_first.temperature
    input_1_max = TPPSPRs_last.temperature
    input_1_info = 'Доступные значения: '+str(input_1_min)+'-'+str(input_1_max)
    input_1_placeholder = input_1_min
    # Все доступные значения давлений
    p = []
    for i in TPPSPRs:
        if float(i.pressure) not in p:
            press = float(i.pressure)
            p.append(press)
    # Соединяем их
    pressures = ', '.join(str(i) for i in p)
    # Добавляем в отображение
    input_2_info = 'Доступные значения: '+pressures
    input_2_placeholder = '0.5'
    info_box_1 = 'Введите значения параметров и нажмите Enter.'
    info_box_2 = 'Сейчас доступен диапазон температур: '+str(input_1_min)+'-'+str(input_1_max)+'К'
    info_box_3 = 'Cо значениями давлений (МПа): '+pressures
    return render(request, 't-prop/TPPSPR_in_point_create.html', locals())


#Таблица x.5 Теплофоизические и переносные свойства веществ в однофазной области с фильтром
def TPPSPR_in_point(request, substance_id):
    substance = Substance.objects.get(pk=substance_id)
    title = 'Результат расчета теплофизических и переносных свойств для '+substance.name+'а в однофазной области'
    # В таблице отбираем значения с substance_id равным переданному значению
    t = request.GET['temperature']
    t = Decimal(t)
    pressure = request.GET['pressure']
    pressure = Decimal(pressure)
    # Находим минимальный объект вещества
    TPPSPRs = TPPSPR.objects.filter(substance=substance_id)

    # Создаем пустой список
    p = []
    # Добавляем элементы со значениями давления
    for i in TPPSPRs:
        if i.pressure not in p:
            p.append(i.pressure)

    v = 0
    for i in p:
        if pressure == i:
            v = 1
            break

    if v == 1:
        TPPSPRs = TPPSPR.objects.filter(substance=substance_id)
        # Получаем первый элемент
        TPPSPRs_first = TPPSPRs.first()
        # Сравниваем значение температуры
        if t < TPPSPRs_first.temperature:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        TPPSPRs = TPPSPR.objects.filter(substance=substance_id, pressure=pressure)
        # Перебираем элементы массива
        for point in TPPSPRs:
            # Если заданная температура равна или превышает заданное значение
            if point.temperature >= t:
                # Присваиваем id
                s = int(point.id)
                # Останавливаем перебор значений
                break
        # Получаем элемент по id
        T2_point = TPPSPR.objects.get(pk=s)
        # Находим предыдущий элемент
        m = s-1
        # Получаем этот элемент
        T1_point = TPPSPR.objects.get(pk=m)
        # Присваиваем температуру первой точке
        t1 = Decimal(T1_point.temperature)
        # Второй точке
        t2 = Decimal(T2_point.temperature)
        # Повторяем это же с другим элементом
        p1 = Decimal(T1_point.density)
        p2 = Decimal(T2_point.density)
        # находим искомое значение
        density = p1+((p2-p1)/(t2-t1))*(t-t1)
        # Энтальпия
        e1 = Decimal(T1_point.enthalpy)
        e2 = Decimal(T2_point.enthalpy)
        enthalpy = e1+((e2-e1)/(t2-t1))*(t-t1)
        # s - Энтропия, кДж/(кг*К)
        en1 = Decimal(T1_point.entropy)
        en2 = Decimal(T2_point.entropy)
        entropy = en1+((en2-en1)/(t2-t1))*(t-t1)
        # Cp - Изобарная теплоемкость, кДж/(кг*К) (Isobaric heat capacity)
        ih1 = Decimal(T1_point.IhHC)
        ih2 = Decimal(T2_point.IhHC)
        IhHC = ih1+((ih2-ih1)/(t2-t1))*(t-t1)
        # Cv - Изохорная теплоемкость, кДж/(кг*К) (Isochonic heat capacity)
        ib1 = Decimal(T1_point.IbHC)
        ib2 = Decimal(T2_point.IbHC)
        IbHC = ib1+((ib2-ib1)/(t2-t1))*(t-t1)
        # λ - Теплопроводность, мВт/(м*К) (Thermal conductivity)    
        tv1 = Decimal(T1_point.TC)
        tv2 = Decimal(T2_point.TC)
        TC = tv1+((tv2-tv1)/(t2-t1))*(t-t1)
        # μ - Динамическая вязкость, Па*с*10^7 (Dynamic viscosity)
        dv1 = Decimal(T1_point.DV)
        dv2 = Decimal(T2_point.DV)
        DV = dv1+((dv2-dv1)/(t2-t1))*(t-t1)
        # Pr - Критерий Прандтля (Criterion of Prandtl)
        cp1 = Decimal(T1_point.CP)
        cp2 = Decimal(T2_point.CP)
        CP = cp1+((cp2-cp1)/(t2-t1))*(t-t1)
        
    if v == 0:
        if (pressure > 1):
            pressure = round(pressure)
        else:
            pressure = round(pressure, 1)
        TPPSPRs = TPPSPR.objects.filter(substance=substance_id, pressure=pressure)
        s = 0
        # Перебираем элементы массива
        for point in TPPSPRs:
            # Если заданная температура равна или превышает заданное значение
            if point.temperature >= t:
                # Присваиваем id
                s = int(point.id)
                # Останавливаем перебор значений
                break
        # Получаем элемент по id
        T2_point = TPPSPR.objects.get(pk=s)
        # Находим предыдущий элемент
        m = s-1
        # Получаем этот элемент
        T1_point = TPPSPR.objects.get(pk=m)
        # Присваиваем температуру первой точке
        t1 = Decimal(T1_point.temperature)
        # Второй точке
        t2 = Decimal(T2_point.temperature)
        # Повторяем это же с другим элементом
        p1 = Decimal(T1_point.density)
        p2 = Decimal(T2_point.density)
        # находим искомое значение
        density = p1+((p2-p1)/(t2-t1))*(t-t1)
        # Энтальпия
        e1 = Decimal(T1_point.enthalpy)
        e2 = Decimal(T2_point.enthalpy)
        enthalpy = e1+((e2-e1)/(t2-t1))*(t-t1)
        # s - Энтропия, кДж/(кг*К)
        en1 = Decimal(T1_point.entropy)
        en2 = Decimal(T2_point.entropy)
        entropy = en1+((en2-en1)/(t2-t1))*(t-t1)
        # Cp - Изобарная теплоемкость, кДж/(кг*К) (Isobaric heat capacity)
        ih1 = Decimal(T1_point.IhHC)
        ih2 = Decimal(T2_point.IhHC)
        IhHC = ih1+((ih2-ih1)/(t2-t1))*(t-t1)
        # Cv - Изохорная теплоемкость, кДж/(кг*К) (Isochonic heat capacity)
        ib1 = Decimal(T1_point.IbHC)
        ib2 = Decimal(T2_point.IbHC)
        IbHC = ib1+((ib2-ib1)/(t2-t1))*(t-t1)
        # λ - Теплопроводность, мВт/(м*К) (Thermal conductivity)    
        tv1 = Decimal(T1_point.TC)
        tv2 = Decimal(T2_point.TC)
        TC = tv1+((tv2-tv1)/(t2-t1))*(t-t1)
        # μ - Динамическая вязкость, Па*с*10^7 (Dynamic viscosity)
        dv1 = Decimal(T1_point.DV)
        dv2 = Decimal(T2_point.DV)
        DV = dv1+((dv2-dv1)/(t2-t1))*(t-t1)
        # Pr - Критерий Прандтля (Criterion of Prandtl)
        cp1 = Decimal(T1_point.CP)
        cp2 = Decimal(T2_point.CP)
        CP = cp1+((cp2-cp1)/(t2-t1))*(t-t1)

        req_pressure = request.GET['pressure']
        req_pressure = Decimal(req_pressure)

        if(req_pressure < pressure):
            if (0.1 < req_pressure < 1):
                pressure_2 = pressure - Decimal(0.1)
            else:
                pressure_2 = pressure - Decimal(1)
        if(req_pressure > pressure):
            if (0.1 < req_pressure < 1):
                pressure_2 = pressure + Decimal(0.1)
            else:
                pressure_2 = pressure + Decimal(1)
        pressure_2 = round(pressure_2, 1)
        # Получаем элемент по id
        T4_point = TPPSPR.objects.get(substance=substance_id, pressure=pressure_2, temperature=T2_point.temperature)
        T3_point = TPPSPR.objects.get(substance=substance_id, pressure=pressure_2, temperature=T1_point.temperature)
        # Присваиваем температуру первой точке
        t3 = Decimal(T3_point.temperature)
        # Второй точке
        t4 = Decimal(T4_point.temperature)
        # Повторяем это же с другим элементом
        p3 = Decimal(T3_point.density)
        p4 = Decimal(T4_point.density)
        # находим искомое значение
        density_2 = p3+((p4-p3)/(t4-t3))*(t-t3)
        # Энтальпия
        e3 = Decimal(T3_point.enthalpy)
        e4 = Decimal(T4_point.enthalpy)
        enthalpy_2 = e3+((e4-e3)/(t4-t3))*(t-t3)
        # s - Энтропия, кДж/(кг*К)
        en3 = Decimal(T3_point.entropy)
        en4 = Decimal(T4_point.entropy)
        entropy_2 = en3+((en4-en3)/(t4-t3))*(t-t3)
        # Cp - Изобарная теплоемкость, кДж/(кг*К) (Isobaric heat capacity)
        ih3 = Decimal(T3_point.IhHC)
        ih4 = Decimal(T4_point.IhHC)
        IhHC_2 = ih3+((ih4-ih3)/(t4-t3))*(t-t3)
        # Cv - Изохорная теплоемкость, кДж/(кг*К) (Isochonic heat capacity)
        ib3 = Decimal(T3_point.IbHC)
        ib4 = Decimal(T4_point.IbHC)
        IbHC_2 = ib3+((ib4-ib3)/(t4-t3))*(t-t3)
        # λ - Теплопроводность, мВт/(м*К) (Thermal conductivity)    
        tv3 = Decimal(T3_point.TC)
        tv4 = Decimal(T4_point.TC)
        TC_2 = tv3+((tv4-tv3)/(t4-t3))*(t-t3)
        # μ - Динамическая вязкость, Па*с*10^7 (Dynamic viscosity)
        dv3 = Decimal(T3_point.DV)
        dv4 = Decimal(T4_point.DV)
        DV_2 = dv3+((dv4-dv3)/(t4-t3))*(t-t3)
        # Pr - Критерий Прандтля (Criterion of Prandtl)
        cp3 = Decimal(T3_point.CP)
        cp4 = Decimal(T4_point.CP)
        CP_2 = cp3+((cp4-cp3)/(t4-t3))*(t-t3)

        if(req_pressure < pressure):
            pr = pressure-pressure_2
            pr_rp = pressure-req_pressure
            density = density_2+((density-density_2)/pr)*pr_rp
            enthalpy = enthalpy_2+((enthalpy-enthalpy_2)/pr)*pr_rp
            entropy = entropy_2+((entropy-entropy_2)/pr)*pr_rp
            IhHC = IhHC_2+((IhHC-IhHC_2)/pr)*pr_rp
            IbHC = IbHC_2+((IbHC-IbHC_2)/pr)*pr_rp
            TC = TC_2+((TC-TC_2)/pr)*pr_rp
            DV = DV_2+((DV-DV_2)/pr)*pr_rp
            CP = CP_2+((CP-CP_2)/pr)*pr_rp
        if(req_pressure > pressure):
            pr = pressure_2-pressure
            pr_rp = req_pressure-pressure
            density = density+((density_2-density)/pr)*pr_rp
            enthalpy = enthalpy+((enthalpy_2-enthalpy)/pr)*pr_rp
            entropy = entropy+((entropy_2-entropy)/pr)*pr_rp
            IhHC = IhHC+((IhHC_2-IhHC)/pr)*pr_rp
            IbHC = IbHC+((IbHC_2-IbHC)/pr)*pr_rp
            TC = TC+((TC_2-TC)/pr)*pr_rp
            DV = DV+((DV_2-DV)/pr)*pr_rp
            CP = CP+((CP_2-CP)/pr)*pr_rp

        pressure = request.GET['pressure']
        pressure = Decimal(req_pressure)

    # TPPSPR_title = 'Теплофоизические и переносные свойства '+substance.name+'а'+' в однофазной области при давлении '+pressure+'МПа'
    return render(request, 't-prop/result.html', locals())  

    