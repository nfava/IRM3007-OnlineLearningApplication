from django.shortcuts import render
from .models import GradeProcess

def grades_dashboard(request):
    grades = GradeProcess.objects.all()

    return render(request, "grades/dashboard.html", {
        "grades": grades
    })
def dashboard(request):
    return render(request, 'grades/dashboard.html')
