from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import SubmissionForm, GPAConverterForm, GradeSubmissionForm, AssignmentForm
from .models import Assignment, Submission

def dashboard(request):
    return render(request, 'dashboard.html')

def grades(request):
    # intakes students name from the search bar and searches their latest first submission
        student_name = request.GET.get('student_name', '')
        submissions = []
        if student_name:
            submissions = Submission.objects.filter(
                student_name__iexact=student_name
            ).select_related('assignment').order_by('-submitted_at')
        return render(request, 'grades.html', {
            'submissions': submissions,
            'student_name': student_name,
        })

def submit_assignment(request):
    # message variable for Late or not
    message = None
    message_type = None
    #Get form and uploaded date
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        #ensure if what user uploaded is valid and save upload time
        #check to make sure if it was submitted on time or no and display respective message
        if form.is_valid():
            submission = form.save(commit=False)
            submission.submitted_at = timezone.now()
            submission.save()
            message = "Submitted successfully!" if not submission.is_late() else "Submitted late! That could affect your grade"
            form = SubmissionForm() #reset form if saved
    else:
        form = SubmissionForm() #reset form if Null

    #get all assignments
    assignments = Assignment.objects.all()
    #Template with daat
    return render(request, 'Assignment_submission.html', {
        'form': form,
        'message': message,
        'assignments': assignments
    })

def professor_dashboard(request):
    submissions = Submission.objects.select_related('assignment').order_by('-submitted_at')
    assignments = Assignment.objects.all().order_by('course_code', 'due_date')

    return render(request, 'professor_dashboard.html', {
        'submissions': submissions,
        'assignments': assignments,
    })

def grade_submission(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)

    if request.method == 'POST':
        form = GradeSubmissionForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            return redirect('professor_dashboard')
    else:
        form = GradeSubmissionForm(instance=submission)

    return render(request, 'grade_submission.html', {
        'form': form,
        'submission': submission
    })


def switch_role(request):
    role = request.POST.get("role")

    if role in ["student", "professor"]:
        request.session["role"] = role

    return redirect(request.META.get("HTTP_REFERER", "dashboard"))


def gpa_converter_view(request):
    return render(request, 'gpa_converter.html')

def view_feedback(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    return render(request, 'feedback.html', {
        'submission': submission
    })
def student_submissions(request):
    student_name = request.GET.get('student_name', '')
    submissions = []
    if student_name:
        submissions = Submission.objects.filter(
            student_name__iexact=student_name
        ).select_related('assignment').order_by('-submitted_at')
    return render(request, 'student_submissions.html', {
        'submissions': submissions,
        'student_name': student_name,
    })
def create_assignment(request):
    # Save new assignment created by professor
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('professor_dashboard')
    else:
        form = AssignmentForm()

    return render(request, 'create_assignment.html', {
        'form': form
    })