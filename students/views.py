from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .models import Student, Lesson
from .forms import StudentForm, LessonForm

def index(request):
    students = Student.objects.all()
    latest_lessons = []

    students_with_empty_lessons = Student.objects.filter(lessons__isnull=True)

    for student in students:
        if student.lessons.exists():
            latest_lesson = student.lessons.latest('date')
            latest_lessons.append(latest_lesson)

    students_and_lessons = zip(students, latest_lessons)
    return render(request, 'students/index.html', {
        'students_and_lessons': students_and_lessons,
        'students_no_lessons': students_with_empty_lessons,
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

def addLesson(request, id):
    student = Student.objects.get(pk=id)
    form = LessonForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            subject = form.cleaned_data['subject']
            date = form.cleaned_data['date']
            paid = form.cleaned_data['paid']
            lesson = Lesson.objects.create(subject=subject, date=date, paid=paid)
            student.lessons.add(lesson)
            return HttpResponseRedirect(reverse('index'))

    return render(request, 'students/add_lesson.html', {'form': form, 'student': student})

def editLesson(request, s_id, l_id):
    student = Student.objects.get(pk=s_id)
    lesson = Lesson.objects.get(pk=l_id)

    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = LessonForm(instance=lesson)

    return render(request, 'students/edit_lesson.html', {
        'form': form,
        'student': student,
        'lesson': lesson,
    })

def deleteLesson(request, id):
    lesson = Lesson.objects.get(pk=id)
    if request.method == 'POST':
        lesson.delete()
        return HttpResponseRedirect(reverse('index'))
    return HttpResponseRedirect(reverse('index'))