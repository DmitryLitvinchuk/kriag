from django.conf.urls import url
from . import views

urlpatterns = [
	#Таблица x.1 Свойства жидкого вещества на линии кипения (по температурам)
    url(r'^PLSBL_T/(?P<substance_id>\d+)/$', views.PLSBL_T_table, name='PLSBL_T_table'),
    #Таблица x.2 Свойства парообразного вещества на линии конденсации (по температурам)
    url(r'^PVSCL_T/(?P<substance_id>\d+)/$', views.PVSCL_T_table, name='PVSCL_T_table'),
    #Таблица x.3 Свойства парообразного вещества на линии кипения (по давлениям)
    url(r'^PLSBL_P/(?P<substance_id>\d+)/$', views.PLSBL_P_table, name='PLSBL_P_table'),
    #Таблица x.4 Свойства парообразного вещества на линии конденсации (по давлениям)
    url(r'^PVSCL_P/(?P<substance_id>\d+)/$', views.PVSCL_P_table, name='PVSCL_P_table'),
	#Таблица x.5 Теплофоизические и переносные свойства веществ в однофазной области
    url(r'^TPPSPR/(?P<substance_id>\d+)/$', views.TPPSPR_table, name='TPPSPR_table'),
    #Таблица x.5 Теплофоизические и переносные свойства веществ в однофазной
    #			  области (с фильтром по давлению)
    url(r'^TPPSPR/(?P<substance_id>\d+)/(?P<pressure>\d+\.\d)$',
    	views.TPPSPR_table_pressure, name='TPPSPR_table_pressure'),

    # url(r'^accounts/register/$', views.RegisterFormView.as_view()),
    # url(r'^accounts/login/$', views.LoginFormView.as_view()),
    # url(r'^accounts/logout/$', views.LogoutView.as_view()),
    # url(r'^accounts/profile/$', views.update_profile, name='update_profile'),
]