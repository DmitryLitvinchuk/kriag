from django.conf.urls import url
from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^accounts/register/$', views.RegisterFormView.as_view()),
    url(r'^accounts/login/$', views.LoginFormView.as_view()),
    url(r'^accounts/logout/$', views.LogoutView.as_view()),
    url(r'^accounts/profile/$', views.update_profile, name='update_profile'),
]