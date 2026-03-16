from django.db import models

# Represents a student
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Represents a course or class
class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.code} - {self.name}"

# Represents the grades for a student in a course
class GradeProcess(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2)
    approved = models.BooleanField(default=False)  # Whether the grade is approved

    def __str__(self):
        return f"{self.student} | {self.course} | {self.grade} | {'Approved' if self.approved else 'Pending'}"