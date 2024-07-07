from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.modelstest,name="models"),
    path('input/',views.input_taker,name="input")    
]
