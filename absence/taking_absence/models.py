from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(verbose_name="Name", max_length=30)
    email = models.EmailField(verbose_name="Email")
    password = models.CharField(verbose_name="Password", max_length=20)


class School(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50)
    director = models.ForeignKey(User, verbose_name="Director", on_delete=models.CASCADE)


class Class(models.Model):
    date = models.DateField(verbose_name="Date")
    start_time = models.TimeField(verbose_name="Start Time")
    end_time = models.TimeField(verbose_name="End Time")


class Student(models.Model):
    school = models.ForeignKey(School, verbose_name="School", on_delete=models.CASCADE)


class Absence(models.Model):
    science = models.ForeignKey(Class, verbose_name="Class", on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)


