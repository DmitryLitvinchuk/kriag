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

"""
Отображение таблицы с веществами
"""
def substances_table(request):
    substances = Substance.objects.all()
    return render(request, 'substances/substances_table.html', {'substances': substances})

