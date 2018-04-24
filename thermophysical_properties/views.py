from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
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

#Таблица x.1 Свойства жидких веществ
def PLSBL_T_table(request, substance_id):
	# В таблице отбираем значения с substance_id равным переданному значению
    PLSBL_Ts = PLSBL_T.objects.filter(substance=substance_id)
    return render(request, 't-prop/plsbl_t_table.html', {'PLSBL_Ts': PLSBL_Ts})

#Таблица x.5 Теплофоизические и переносные свойства веществ в однофазной области
def TPPSPR_table(request, substance_id):
	# В таблице отбираем значения с substance_id равным переданному значению
    TPPSPRs = TPPSPR.objects.filter(substance=substance_id)
    return render(request, 't-prop/tppsprs_table.html', {'TPPSPRs': TPPSPRs})