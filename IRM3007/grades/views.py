from django.shortcuts import render
from .models import GradeProcess

def dashboard(request):
    grades = GradeProcess.objects.all()
    return render(request, 'grades/dashboard.html', {'grades': grades})

def gpa_converter_view(request):

    return render(request, 'grades/gpa_converter.html', {})