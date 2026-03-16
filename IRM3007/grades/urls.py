from django.urls import path
from . import views

urlpatterns = [
    path('', views.grades_dashboard, name='grades_dashboard'),
]