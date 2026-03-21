from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def grades(request):
    return render(request, 'grades.html')

def gpa(request):
    return render(request, 'gpa_converter.html')