from django.db import models
# Assignment model (set by admin) to ensure submission is before date
class Assignment(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateTimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

# Submission model (uploaded by student)
class Submission(models.Model):
    student_name = models.CharField(max_length=100)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    file = models.FileField(upload_to='submissions/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def is_late(self):
        return self.submitted_at > self.assignment.due_date