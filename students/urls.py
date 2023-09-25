from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_student, name='view_student'), 
    path('add/', views.add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('add_lesson/<int:id>', views.addLesson, name='add_lesson'),
    path('edit_lesson/<int:s_id>/<int:l_id>', views.editLesson, name='edit_lesson'),
    path('delete_lesson/<int:id>', views.deleteLesson, name='delete_lesson')
]
