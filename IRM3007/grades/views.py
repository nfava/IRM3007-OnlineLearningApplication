from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.utils import timezone
from .forms import SubmissionForm, GradeSubmissionForm, AssignmentForm
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

    # Search and filtering
    search_query = request.GET.get('q', '').strip()
    course_filter = request.GET.get('course', '').strip()
    status_filter = request.GET.get('status', '').strip()
    grade_filter = request.GET.get('grade_filter', '').strip()
    late_filter = request.GET.get('late_filter', '').strip()

    # Search by student name, assignment title, or course code
    if search_query:
        submissions = submissions.filter(
            Q(student_name__icontains=search_query) |
            Q(assignment__title__icontains=search_query) |
            Q(assignment__course_code__icontains=search_query)
        )

    # Filter by course
    if course_filter:
        submissions = submissions.filter(assignment__course_code=course_filter)

    # Filter by grading workflow status
    if status_filter:
        submissions = submissions.filter(status=status_filter)

    # Filter by graded / not graded
    if grade_filter == 'graded':
        submissions = submissions.filter(grade__isnull=False)
    elif grade_filter == 'not_graded':
        submissions = submissions.filter(grade__isnull=True)

    # Filter by on-time / late
    now = timezone.now()
    if late_filter == 'late':
        submissions = submissions.filter(submitted_at__gt=models.F('assignment__due_date'))
    elif late_filter == 'on_time':
        submissions = submissions.filter(submitted_at__lte=models.F('assignment__due_date'))

    # Get unique course codes for dropdown
    course_codes = Assignment.objects.values_list('course_code', flat=True).distinct().order_by('course_code')

    return render(request, 'professor_dashboard.html', {
        'submissions': submissions,
        'assignments': assignments,
        'course_codes': course_codes,
        'search_query': search_query,
        'selected_course': course_filter,
        'selected_status': status_filter,
        'selected_grade_filter': grade_filter,
        'selected_late_filter': late_filter,
        'status_choices': Submission.STATUS_CHOICES,
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