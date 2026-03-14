from django.db import models
from django.contrib.auth.models import User

class GradeProcess(models.Model):

    STATUS_CHOICES = [
        ('submitted', 'Exam/Assignment Submitted'),
        ('written', 'Exam Written'),
        ('grading', 'Professor Grading'),
        ('dean_review', 'Final Grades Submitted to Dean'),
        ('approved', 'Grades Approved'),
        ('released', 'Grades Released')
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    submission_date = models.DateTimeField()
    is_late = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} - {self.course}"