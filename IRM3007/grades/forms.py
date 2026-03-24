from django import forms
from .models import Submission, Assignment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TaskForm(forms.ModelForm):
    class Meta:
        fields = ['username', 'email', 'password1', 'password2']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
#feild for student to add their name and course they are working on
class SubmissionForm(forms.ModelForm):
    student_name = forms.CharField(max_length=100, label="Your Name")
    course_code = forms.CharField(max_length=10, required=False, label="Course Code")

# What is included in submission feilds
    class Meta:
        model = Submission
        fields = ['course_code','student_name', 'assignment', 'file']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        assignments = Assignment.objects.all()
        #Setting id values that are unique and can be called
        self.fields['assignment'].widget.attrs.update({'id': 'id_assignment'})
        self.fields['course_code'].widget.attrs.update({'id': 'id_course_code'})

        #setting bar as "select assignment" and allowing use to select from all assignments in that course
        self.fields['assignment'].empty_label = "Select Assignment"
        self.fields['assignment'].choices = [('', 'Select Assignment')] + [
        (a.id, f"{a.title} ({a.course_code})")
        for a in assignments
        ]


CONVERSION_CHOICES = [
    ("percent_to_all", "Percentage → Letter + 12-point + 4-point"),
    ("gpa12_to_gpa4", "12-point GPA → 4-point GPA"),
]

class GPAConverterForm(forms.Form):
    conversion_type = forms.ChoiceField(
        choices=CONVERSION_CHOICES,
        label="Conversion Type"
    )

    percentage = forms.FloatField(
        required=False,
        min_value=0,
        max_value=100,
        label="Percentage"
    )

    gpa_12 = forms.FloatField(
        required=False,
        min_value=0,
        max_value=12,
        label="12-point GPA"
    )

