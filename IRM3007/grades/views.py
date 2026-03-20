from django.shortcuts import render
from .models import GradeProcess

def dashboard(request):
    grades = GradeProcess.objects.all()
    return render(request, 'dashboard.html', {'grades': grades})

def gpa_converter_view(request):
    return render(request, 'gpa_converter.html', {})