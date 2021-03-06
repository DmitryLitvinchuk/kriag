from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.acdas_table, name='acdas_table'),
    url(r'^accounts/register/$', views.RegisterFormView.as_view()),
    url(r'^accounts/login/$', views.LoginFormView.as_view()),
    url(r'^accounts/logout/$', views.LogoutView.as_view()),
    url(r'^accounts/profile/$', views.update_profile, name='update_profile'),
]