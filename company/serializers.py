from rest_framework import serializers
from TestDRF.wsgi import *
from company.models import Employee, Department


# Сериалайзер сотрудников
class EmployeeModelSerializer(serializers.ModelSerializer):
    # Вывод всех существующих полей каждого сотрудника
    class Meta:
        model = Employee
        fields = '__all__'


# Сериалайзер для департаментов
class DepartmentModelSerializer(serializers.ModelSerializer):
    # Количество сотрудников
    employees_count = serializers.IntegerField(read_only=True)
    # Суммарный оклад всех сотрудников
    full_salary = serializers.DecimalField(read_only=True, max_digits=30, decimal_places=2)

    class Meta:
        model = Department
        # Поля указанные в ТЗ. Стандарные 2 и + количество сотрудников и суммарный оклад
        fields = [
            'name',
            'director',
            'employees_count',
            'full_salary'
        ]
