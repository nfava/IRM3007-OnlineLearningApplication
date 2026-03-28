from django import forms
from .models import Submission, Assignment

#feild for student to add their name and course they are working on
class SubmissionForm(forms.ModelForm):
    student_name = forms.CharField(max_length=100, label="Your Name")
    course_code = forms.CharField(max_length=10, required=False, label="Course Code")

# What is included in submission feilds all values we use later!
    class Meta:
        model = Submission
        fields = ['student_name', 'assignment', 'file', 'course_code']
#will run when form is created, how we customize the drop down and call all assignments 
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

# Professor grading form
class GradeSubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['grade', 'feedback','status']

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'course_code', 'due_date', 'instruction_file']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

