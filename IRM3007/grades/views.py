from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import SubmissionForm, GPAConverterForm, GradeSubmissionForm
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
    return render(request, 'professor_dashboard.html', {
        'submissions': submissions
    })

def grade_submission(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)

    if request.method == 'POST':
        form = GradeSubmissionForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
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

# Grades Converter
# Convert percentage to letter grade
def percentage_to_letter_and_gpa12(percentage: float):
    if percentage >= 90:
        return "A+", 12
    elif percentage >= 85:
        return "A", 11
    elif percentage >= 80:
        return "A-", 10
    elif percentage >= 77:
        return "B+", 9
    elif percentage >= 73:
        return "B", 8
    elif percentage >= 70:
        return "B-", 7
    elif percentage >= 67:
        return "C+", 6
    elif percentage >= 63:
        return "C", 5
    elif percentage >= 60:
        return "C-", 4
    elif percentage >= 57:
        return "D+", 3
    elif percentage >= 53:
        return "D", 2
    elif percentage >= 50:
        return "D-", 1
    else:
        return "F", 0

# Convert 12 to 4 GPA
def gpa12_to_gpa4(gpa12: float):
    return round((gpa12 / 12) * 4, 2)


def gpa_converter_view(request):
    form = GPAConverterForm(request.POST or None)
    result = None
    error_message = None

    if request.method == "POST" and form.is_valid():
        conversion_type = form.cleaned_data["conversion_type"]
        percentage = form.cleaned_data.get("percentage")
        gpa_12 = form.cleaned_data.get("gpa_12")

        if conversion_type == "percent_to_all":
            if percentage is None:
                error_message = "Please enter a percentage value."
            else:
                letter, gpa12 = percentage_to_letter_and_gpa12(percentage)
                gpa4 = gpa12_to_gpa4(gpa12)
                result = {
                    "input_type": "Percentage",
                    "input_value": percentage,
                    "letter_grade": letter,
                    "gpa_12": gpa12,
                    "gpa_4": gpa4,
                }

        elif conversion_type == "gpa12_to_gpa4":
            if gpa_12 is None:
                error_message = "Please enter a 12-point GPA value."
            else:
                result = {
                    "input_type": "12-point GPA",
                    "input_value": gpa_12,
                    "gpa_4": gpa12_to_gpa4(gpa_12),
                }

    return render(
        request,
        "gpa_converter.html",
        {
            "form": form,
            "result": result,
            "error_message": error_message,
        },
    )
def view_feedback(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    return render(request, 'feedback.html', {
        'submission': submission
    })