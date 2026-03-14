from django.shortcuts import render
from .models import GradeProcess

def grades_dashboard(request):

    grade_process = GradeProcess.objects.filter(student=request.user)

    return render(request, "grades/dashboard.html", {
        "grades": grade_process
    })