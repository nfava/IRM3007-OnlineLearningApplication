from django.shortcuts import render
from .models import GradeProcess

def dashboard(request):
    grades = GradeProcess.objects.all()

    return render(request, 'grades/dashboard.html', {
        'grades': grades
    })
