from django.urls import path
from django.urls import include
from django.conf import settings
from ViloSkyApp import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('mydetails/',views.mydetails, name='mydetails'),
    path('myactions/',views.myactions, name='myactions'),
    path('report/',views.report, name='report'),
    path('roles/',views.roles, name='roles'),
    path('input/',views.input, name='input'),
    path('output/',views.output, name='output'),
    path('data/',views.data, name='data'),
    path('editquestion/',views.editquestion, name='editquestion'),
    path('outputdetails/',views.outputdetails, name='outputdetails'),
    path('logout/', views.user_logout, name='logout'),
    path('input_form/',views.inputform, name='input_form'),
]