from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('patients/', views.patient_list, name='patients'),
    path('appointments/', views.appointments, name='appointments'),
]