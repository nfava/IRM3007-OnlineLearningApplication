from django import forms
from .models import Submission, Assignment

class SubmissionForm(forms.ModelForm):
    course_code = forms.CharField(max_length=10, required=False, label="Course Code")

    class Meta:
        model = Submission
        fields = ['course_code', 'assignment', 'file']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        assignments = Assignment.objects.all()
        self.fields['assignment'].widget.attrs.update({'id': 'id_assignment'})
        self.fields['course_code'].widget.attrs.update({'id': 'id_course_code'})
        self.fields['assignment'].choices = [
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

