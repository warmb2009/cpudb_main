from django.urls import path
from . import views

app_name = 'cpuapi'
urlpatterns = [
    path(r'cpu/', views.Cpu.as_view()),
    path(r'cpud/<cpuid>/', views.CpuDetail.as_view()),
    path(r'getonecpu/', views.CpuGet.as_view()),
    path(r'travelcpu/', views.CpuTravel.as_view()),
    path(r'getcpu/<cpu_name>/', views.CpuTravel.as_view()),
]
