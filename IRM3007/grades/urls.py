from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('grades/', views.grades, name='grades'),
    path('converter/', views.gpa_converter_view, name='converter'),
    path('submit/', views.submit_assignment, name='submit'),
    path("switch-role/", views.switch_role, name="switch_role"),
    path('submission/<int:submission_id>/grade/', views.grade_submission, name='grade_submission'),
]