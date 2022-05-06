from django.db.models import Model, CharField, PositiveIntegerField, DateTimeField, BooleanField, IntegerField


class Person(Model):
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    age = PositiveIntegerField()
    STUDENT = 'STD'
    TEACHER = 'TCH'
    PERSON_TYPE_CHOICES = [
        (STUDENT, 'STD'),
        (TEACHER, 'TCH'),
    ]
    person_type = CharField(max_length=3, choices=PERSON_TYPE_CHOICES, default=STUDENT)
    creation_time = DateTimeField(auto_now_add=True)
    update_time = DateTimeField(auto_now=True)
    active_acc = BooleanField(default=True)


class Group(Model):
    group_name = CharField(max_length=4)
    students = IntegerField()
    headman = IntegerField()
    edu_program = CharField(max_length=100)
    creation_time = DateTimeField(auto_now_add=True)
    update_time = DateTimeField(auto_now=True)


class Subject(Model):
    teachers = IntegerField()
    creation_time = DateTimeField(auto_now_add=True)
    update_time = DateTimeField(auto_now=True)


class Course(Model):
    course_headman = IntegerField()
    curator = IntegerField()
    subjects = IntegerField()
    groups = IntegerField()
    creation_time = DateTimeField(auto_now_add=True)
    update_time = DateTimeField(auto_now=True)


class Lesson(Model):
    subject = IntegerField()
    teacher = IntegerField()
    theme = CharField(max_length=100)
    groups = IntegerField()
    creation_time = DateTimeField(auto_now_add=True)
    update_time = DateTimeField(auto_now=True)
