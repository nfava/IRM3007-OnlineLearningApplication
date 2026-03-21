from django.shortcuts import render
from django.utils import timezone
from .forms import SubmissionForm
from .models import Assignment

def dashboard(request):
    return render(request, 'dashboard.html')

def grades(request):
    return render(request, 'grades.html')

def gpa(request):
    return render(request, 'gpa_converter.html')

def submit_assignment(request):
    message = None
    message_type = None
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.submitted_at = timezone.now()
            submission.save()
            message = "Submitted successfully!" if not submission.is_late() else "Submitted late! That could affect your grade"
            message_type = "late" if submission.is_late() else "success"
            form = SubmissionForm()
    else:
        form = SubmissionForm()

    assignments = Assignment.objects.all()
    return render(request, 'Assignment_submission.html', {
        'form': form,
        'message': message,
        'message_type': message_type,
        'assignments': assignments
    })