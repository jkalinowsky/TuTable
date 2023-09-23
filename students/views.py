from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Student, Lesson
from .forms import StudentForm

def index(request):
    students = Student.objects.all()
    latest_lessons = []

    for student in students:
        latest_lesson = student.lessons.latest('date')
        latest_lessons.append(latest_lesson)

    students_and_lessons = zip(students, latest_lessons)
    return render(request, 'students/index.html', {
        'students_and_lessons': students_and_lessons,
    })

def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_telephone_number = form.cleaned_data['telephone_number']
            new_tutor_subject = form.cleaned_data['tutor_subject']

            new_student = Student(
                student_number = new_student_number,
                first_name = new_first_name,
                last_name = new_last_name,
                telephone_number = new_telephone_number,
                tutor_subject = new_tutor_subject
            )
            new_student.save()
            return render(request, 'students/add.html', {
                'form': StudentForm(),
                'success': True
            })
    else:
        form = StudentForm()
    return render(request, 'students/add.html', {
        'form': StudentForm()
    })    


def edit(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit.html', {
                'form': form,
                'success': True
            })
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
    return render(request, 'students/edit.html', {
        'form': form
    })


def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))
