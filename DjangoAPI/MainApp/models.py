from django.db import models

# Create your models here

class Departments(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=500)

class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=500)
    department = models.ForeignKey(Departments, on_delete=models.DO_NOTHING)
    date_of_hire = models.DateField()
    photo_file_name = models.CharField(max_length=500)