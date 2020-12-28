from django.urls import path
from django.urls import include
from django.conf import settings
from ViloSkyApp import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
]