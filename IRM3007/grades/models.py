from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Assignment model (set by admin) allows admin (prof to set due date which with cross check with submission date)
class Assignment(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateTimeField()
    course_code = models.CharField(max_length=10)  # field for course code
    instruction_file = models.FileField(upload_to='instructions/', blank=True, null=True) # th
    def __str__(self):
        return f"{self.course_code} - {self.title}"


# Submission model (uploaded by student) checks to see when it was submitted "at" vs set due date
#uploads to submission folder, within media
class Submission(models.Model):
    student_name = models.CharField(max_length=100)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    file = models.FileField(upload_to='submissions/')
    # save the time it was submitted to check vs admin set due date
    submitted_at = models.DateTimeField(auto_now_add=True)

    # Professor feedback
    grade = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, validators=[ MinValueValidator(0), MaxValueValidator(100) ])
    feedback = models.TextField(blank=True, null=True)

    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('under_review', 'Under Review'),
        ('final_approval', 'Final Approval'),
        ('released', 'Released'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='not_started'
    )

    # result a student will get if submission is late
    #views displays on time or late message based on this result
    def is_late(self):
        return self.submitted_at > self.assignment.due_date