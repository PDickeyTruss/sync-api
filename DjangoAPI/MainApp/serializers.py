from rest_framework import serializers
from MainApp.models import Departments, Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields=('department_id', 'department_name')

class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)    
    class Meta:
        model=Employees
        fields=('employee_id', 'employee_name', 'department', 'date_of_hire')
        optional_fields=('PhotoFileName')
class EmployeeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=('employee_id', 'employee_name', 'department', 'date_of_hire')
        optional_fields=('PhotoFileName')