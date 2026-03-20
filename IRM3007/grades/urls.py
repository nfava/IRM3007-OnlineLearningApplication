from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('converter/', views.gpa_converter_view, name='gpa_converter'),
]