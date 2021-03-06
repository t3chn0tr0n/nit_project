from django.db import models
from django.utils import timezone

from subject_and_marks.models import SemMarks
from teachers.models import Teacher


class Student(models.Model):
    id = models.CharField(default=" ", max_length=15, primary_key=True)
    name = models.CharField(default=" ", max_length=50) #First Name
    middle_name = models.CharField(default=" ", max_length=50) # Middle name
    surname = models.CharField(default=" ", max_length=50) # Last name
    mentor = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    univ_roll_no = models.CharField(default=" ", max_length=20, null=True) # This is a unique field, candidate key!
    registration_no = models.CharField(default=" ", max_length=20, null=True)
    admission_no = models.CharField(default=" ", max_length=20, null=True) # last 3 digits = class roll no.
    dept = models.CharField(default=" ", max_length=20)  # stores as CSE, ECE
    stream = models.CharField(default=" ", max_length=1) # B or M or D
    batch = models.CharField(default="", max_length=12)  # stores BAT20152019
    is_registered = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    email = models.EmailField(max_length=70)
    is_lateral = models.BooleanField(default=False)
    has_certificate = models.BooleanField(default=False)
    certificate = models.CharField(default=" ", max_length=20, null=True)

class Details(models.Model):
    card_no = models.CharField(default=" ", max_length=15, primary_key=True)
    dob = models.DateField(default=timezone.now)
    blood_grp = models.CharField(default="", max_length=3)
    guardian = models.CharField(default="", max_length=50)
    perm_add = models.CharField(default="", max_length=50)  # permanent address
    loc_guardian = models.CharField(default="", max_length=50)
    loc_add = models.CharField(default="", max_length=50)
    land_phone = models.CharField(default="", max_length=11)
    guardian_mobile_no =  models.CharField(default="", max_length=10)
    mobile_no = models.CharField(default="", max_length=10)
    diploma_score = models.FloatField(max_length="50", null=True)

    # returns a dictionary object of student, ready to be serialized
    def student_details_data(self):
        pass

class Batch(models.Model):
    id = models.CharField(default=" ", max_length=15, primary_key=True)
    batch = models.CharField(default="", max_length=15,null=False)


class ExtracurricularActivity(models.Model):
    student = models.CharField(default=" ", max_length=15, primary_key=True)
    soft_skill_conduct = models.IntegerField(default=0)
    soft_skill_attend = models.IntegerField(default=0)
    aptitude_conduct = models.IntegerField(default=0)
    aptitude_attend = models.IntegerField(default=0)
    mock_interview = models.BooleanField(default=False)
    online_test = models.BooleanField(default=False)
    gate_exam = models.BooleanField(default=False)
    cat_exam = models.BooleanField(default=False)
    saraswati_puja = models.BooleanField(default=False)
    vishwakarma_puja = models.BooleanField(default=False)
    industry_visit_1 = models.CharField(default="", max_length=50)
    industry_visit_1_date = models.DateField(null=True)
    industry_visit_2 = models.CharField(default="", max_length=50)
    industry_visit_2_date = models.DateField(null=True)


class SeminarsWorkshops(models.Model):
    attendee = models.CharField(default=" ", max_length=15)
    name = models.CharField(default="", max_length=50)
    date = models.DateField(default=timezone.now)
    organiser = models.CharField(default="", max_length=50)


class Contributions(models.Model):
    student = models.CharField(default=" ", max_length=15, primary_key=True)
    contributions = models.TextField(default="")
    annual_magazine_paper = models.TextField(default="")
    annual_magazine_event = models.TextField(default="")
    wall_magazine_paper = models.TextField(default="")
    wall_magazine_event = models.TextField(default="")
    technical_academic_awards = models.TextField(default="")
    technical_contests = models.TextField(default="")
    paper_publication = models.TextField(default="")
    

class Class10(models.Model):
    student = models.CharField(default=" ", max_length=15, primary_key=True)
    medium = models.CharField(default="", max_length=20)
    school_name = models.CharField(default="", max_length=50)
    passing_year = models.CharField(default="0000", max_length=4)
    school_address = models.CharField(default="", max_length=100)
    score = models.FloatField(default=0.0)
    achievements = models.CharField(default="", max_length=1000)


class Class12(models.Model):
    student = models.CharField(default=" ", max_length=15, primary_key=True)
    medium = models.CharField(default="", max_length=20)
    school_name = models.CharField(default="", max_length=50)
    passing_year = models.CharField(default="0000", max_length=4)
    school_address = models.CharField(default="", max_length=100)
    score = models.FloatField(default=0.0)
    achievements = models.CharField(default="", max_length=1000)


class FormFills(models.Model):
    student = models.CharField(default=" ", max_length=15, primary_key=True)
    is_gen_details_filled = models.BooleanField(default=False)
    is_univ_details_filled = models.BooleanField(default=False)
    is_sem1_filled = models.BooleanField(default=False)
    is_sem2_filled = models.BooleanField(default=False)
    is_sem3_filled = models.BooleanField(default=False)
    is_sem4_filled = models.BooleanField(default=False)
    is_sem5_filled = models.BooleanField(default=False)
    is_sem6_filled = models.BooleanField(default=False)
    is_sem7_filled = models.BooleanField(default=False)
    is_sem8_filled = models.BooleanField(default=False)

    def sem_fills_easy(self):
        sems = {
            "1": self.is_sem1_filled,
            "2": self.is_sem2_filled,
            "3": self.is_sem3_filled,
            "4": self.is_sem4_filled,
        }
        if Student.objects.get(id=self.student).stream in ('B', 'D') :
            sems["5"] =  self.is_sem5_filled
            sems["6"] =  self.is_sem6_filled
        if Student.objects.get(id=self.student).stream == 'B':
            sems["7"] =  self.is_sem7_filled
            sems["8"] =  self.is_sem8_filled
        return sems


class Counselings(models.Model):
    student = models.CharField(default=" ", max_length=15)
    date = models.DateField(default=timezone.now)
    topic = models.CharField(default=" ", max_length=30)