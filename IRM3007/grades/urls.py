from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('grades/', views.grades, name='grades'),
    path('converter/', views.gpa_converter_view, name='converter'),
    path('submit/', views.submit_assignment, name='submit'),
    path("switch-role/", views.switch_role, name="switch_role"),
    path('submission/<int:submission_id>/grade/', views.grade_submission, name='grade_submission'),
    path('professor-dashboard/', views.professor_dashboard, name='professor_dashboard'),
    path('submission/<int:submission_id>/feedback/', views.view_feedback, name='view_feedback'),
]