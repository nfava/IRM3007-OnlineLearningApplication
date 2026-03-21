from django.shortcuts import render
from django.utils import timezone
from .forms import SubmissionForm
from .models import Submission

def dashboard(request):
    return render(request, 'dashboard.html')

def grades(request):
    return render(request, 'grades.html')

def gpa(request):
    return render(request, 'gpa_converter.html')

def submit_assignment(request):
    message = 'test'
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.submitted_at = timezone.now()
            submission.save()
            message = "Submitted successfully!" if not submission.is_late() else "Submitted, but after the due date!"
            form = SubmissionForm()  # Clear form
    else:
        form = SubmissionForm()
    return render(request, 'Assignment_submission.html', {'form': form, 'message': message})