from django.core.exceptions import ValidationError


# Сотрудник не может стать директором
def validate_director(value):
    from company.models import Employee
    if not Employee.objects.filter(id=value, position=Employee.d).exists():
        raise ValidationError('Сотрудник не является директором')
