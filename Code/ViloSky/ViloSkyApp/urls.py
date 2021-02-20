''' URLs for the ViloSky project '''
from django.urls import path, re_path
from ViloSkyApp import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

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
    path('reset-password/', PasswordResetView.as_view(), name='password_reset'),
    path('reset-password/done', PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset-password/confirm/<uidb64>[0-9A-Za-z]+)-<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/', PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
