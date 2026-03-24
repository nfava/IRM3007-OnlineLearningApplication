from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('accounts/login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('grades/', views.grades, name='grades'),
    path('converter/', views.gpa_converter_view, name='converter'),
    path('submit/', views.submit_assignment, name='submit')
]