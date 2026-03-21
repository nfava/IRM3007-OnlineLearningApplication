from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('grades/', views.grades, name='grades'),
    path('converter/', views.gpa, name='converter'),
    path('submit/', views.submit_assignment, name='submit')
]