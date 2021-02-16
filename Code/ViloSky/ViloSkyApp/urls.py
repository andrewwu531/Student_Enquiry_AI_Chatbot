from django.urls import path, re_path
from django.urls import include
from django.conf import settings
from ViloSkyApp import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('mydetails/', views.mydetails, name='mydetails'),
    re_path('action/(?P<action_id>\w+)/$', views.action, name='action'),
    path('actions/', views.actions, name='actions'),
    re_path('report/(?P<report_id>\w+)/$', views.report, name='report'),
    path('reports/', views.reports, name='reports'),
    path('roles/', views.roles, name='roles'),
    re_path('admin_input/(?P<admin_input_id>\w+)/$',
            views.admin_input, name='admin_input'),
    path('admin_inputs/', views.admin_inputs, name='admin_inputs'),
    path('output/', views.output, name='output'),
    path('data/', views.data, name='data'),
    path('outputdetails/', views.outputdetails, name='outputdetails'),
    path('logout/', views.user_logout, name='logout'),
]
