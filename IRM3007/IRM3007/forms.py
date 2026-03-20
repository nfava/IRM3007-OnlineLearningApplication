from django import forms

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