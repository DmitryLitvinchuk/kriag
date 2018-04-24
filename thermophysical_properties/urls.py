from django.conf.urls import url
from . import views

urlpatterns = [
	#Таблица x.1 Свойства жидких веществ
    url(r'^PLSBL_T/(?P<substance_id>\d+)/$', views.PLSBL_T_table, name='PLSBL_T_table'),
	#Таблица x.5 Теплофоизические и переносные свойства веществ в однофазной области
    url(r'^TPPSPR/(?P<substance_id>\d+)/$', views.TPPSPR_table, name='TPPSPR_table'),
    # url(r'^accounts/register/$', views.RegisterFormView.as_view()),
    # url(r'^accounts/login/$', views.LoginFormView.as_view()),
    # url(r'^accounts/logout/$', views.LogoutView.as_view()),
    # url(r'^accounts/profile/$', views.update_profile, name='update_profile'),
]