from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=10)
    student_id = models.CharField(max_length=20, primary_key=True)
    student_email = models.EmailField(max_length=50)
    student_branch = models.CharField(max_length=20)
    student_contact = models.CharField(max_length=20)
    student_password = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name = 'Student Information'
        verbose_name_plural = 'Student Informations'

    def __str__(self):
        return self.student_name