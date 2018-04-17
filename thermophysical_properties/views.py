# from django.shortcuts import render, redirect
# from django.utils import timezone
# from .models import Post, User, Profile, ACDA
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

# """
# Отображение таблицы 1.1
# Усредненный состав воздуха
# """
# def acdas_table(request):
#     acdas = ACDA.objects.all()
#     return render(request, 'blog/acdas_table.html', {'acdas': acdas})


# class RegisterFormView(FormView):
#     form_class = UserCreationForm

#     # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
#     # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
#     success_url = "accounts/login/"

#     # Шаблон, который будет использоваться при отображении представления.
#     template_name = "blog/register.html"

#     def form_valid(self, form):
#         # Создаём пользователя, если данные в форму были введены корректно.
#         form.save()

#         # Вызываем метод базового класса
#         return super(RegisterFormView, self).form_valid(form)


# class LoginFormView(FormView):
#     form_class = AuthenticationForm

#     # Аналогично регистрации, только используем шаблон аутентификации.
#     template_name = "blog/login.html"

#     # В случае успеха перенаправим на главную.
#     success_url = "/"

#     def form_valid(self, form):
#         # Получаем объект пользователя на основе введённых в форму данных.
#         self.user = form.get_user()

#         # Выполняем аутентификацию пользователя.
#         login(self.request, self.user)
#         return super(LoginFormView, self).form_valid(form)

# class LogoutView(View):
#     def get(self, request):
#         # Выполняем выход для пользователя, запросившего данное представление.
#         logout(request)

#         # После чего, перенаправляем пользователя на главную страницу.
#         return HttpResponseRedirect("/")

# @login_required
# @transaction.atomic
# def update_profile(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, ('Your profile was successfully updated!'))
#             return redirect('post_list')
#         else:
#             messages.error(request, _('Please correct the error below.'))
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'blog/profile.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })