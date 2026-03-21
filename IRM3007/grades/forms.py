from django import forms
from .models import Submission


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['student_name', 'assignment', 'file']

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            if not file.name.endswith(('.pdf', '.doc', '.docx')):
                raise forms.ValidationError("Only PDF or Word files allowed.")
        return file


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

