from django.db import models

class Lesson(models.Model):
    subject = models.CharField(max_length=255)
    date = models.DateField()

class Student(models.Model):
    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    telephone_number = models.CharField(max_length=12)
    lessons = models.ManyToManyField(Lesson)
    tutor_subject = models.CharField(max_length=50)
    
    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'
