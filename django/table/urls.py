from django.urls import path

from table import views

urlpatterns = [
    path('', views.index),
    path('table_ajax', views.table_ajax, name='table_ajax')
]