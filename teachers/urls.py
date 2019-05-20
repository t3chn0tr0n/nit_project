from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('student_csv_upload/', upload_student, name="upload_student"),
    path('student_csv_upload/upload_student/', upload_student),
    path('search', student_search, name="search"),
    path('mentees/', mentees_list, name="mentees_list"),
    re_path(r'view_student/(NIT\/([2-9][0-9][0-9][0-9])\/([0-9][0-9][0-9][0-9]))', view_student, name="view_student"),
    path('princi_teacher_view/', princi_teacher_view, name="princi_teacher_view"),
    path('princi_teacher_view/assign_hod/', assign_hod, name="assign_hod"),
]
