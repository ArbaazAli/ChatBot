from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=10)
    student_id = models.CharField(max_length=20, default=False)
    student_email = models.EmailField(max_length=50, default=False)
    student_branch = models.CharField(max_length=20, default=False)
    student_contact = models.CharField(max_length=20, default=False)
    password = models.CharField(max_length=100, default=False)
    confirm_password = models.CharField(max_length=300, default=False)

    class Meta:
        verbose_name = 'Student Information'
        verbose_name_plural = 'Student Informations'

    def __str__(self):
        return self.student_name