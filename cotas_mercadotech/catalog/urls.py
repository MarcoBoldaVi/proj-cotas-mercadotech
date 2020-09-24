from django.urls import path
from catalog import views
from django.conf.urls import include


urlpatterns = [
    path('', views.index),
]