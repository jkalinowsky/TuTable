from django import forms
from .models import Student, Lesson

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number', 'first_name', 'last_name', 'telephone_number', 'tutor_subject']
        labels = {
            'student_number': 'Student Number',
            'first_name': 'First Name', 
            'last_name': 'Last Name', 
            'telephone_number': 'Phone Number', 
            'tutor_subject': 'Tutoring Subject'
        }
        widgets = {
            'student_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'tutor_subject': forms.TextInput(attrs={'class': 'form-control'})
        }

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['subject', 'date', 'paid']
        labels = {
            'subject': 'Lesson Subject',
            'date': 'Lesson Date',
            'paid': 'Was the lesson paid?'
        }
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
        }