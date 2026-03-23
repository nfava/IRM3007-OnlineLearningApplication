from django.shortcuts import render

def dashboard(request):
    # Add data to context if you want to display things
    context = {}
    return render(request, 'Projectsettings/dashboard.html', context)