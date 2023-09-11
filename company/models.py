from django.core.exceptions import ValidationError
from django.db import models
from company.validators import validate_director


# Таблица сотрудников
class Employee(models.Model):
    # Разделение сотрудника и директора
    e = 1
    d = 2
    position = (
        (e, 'Работник'),
        (d, 'Директор')
    )
    # Необходимые поля таблицы по ТЗ
    first_name = models.CharField(verbose_name='Имя', max_length=40, blank=False)
    last_name = models.CharField(verbose_name='Фамилия', max_length=40, db_index=True, blank=False)
    middle_name = models.CharField(verbose_name='Отчество', max_length=40, blank=True)
    position = models.PositiveSmallIntegerField(choices=position, verbose_name='Должность', blank=False)
    salary = models.DecimalField(verbose_name='Оклад', max_digits=15, decimal_places=2, blank=False)
    department = models.ForeignKey('company.Department', verbose_name='Департамент', on_delete=models.CASCADE,
                                   related_name='employees')
    photo = models.ImageField(upload_to='images/', verbose_name='Фото', blank=True)

    class Meta:
        verbose_name = 'Сотрудника'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.position}'

    # full_clean(), - это очистка каждого отдельного поля.
    def full_clean(self, exclude=None, validate_unique=True, **kwargs):
        return super(Employee, self).full_clean()

    # Этот метод похож на clean_fields(), но проверяет все ограничения уникальности вашей модели, а не отдельные
    # значения полей. Необходимо было добавить разделение сотрудника и директора и проверку, что сотрудник != директор
    def validate_unique(self, **kwargs):
        super(Employee, self).validate_unique(**kwargs)
        if self.position == self.d and self.department.director:
            raise ValidationError('У департамента уже есть директор!')


# Таблица департамент
class Department(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50, blank=False)
    director = models.OneToOneField(Employee, verbose_name='Директор', on_delete=models.SET_NULL, null=True,
                                    validators=[validate_director], related_name='director', blank=True,
                                    )

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'

    def __str__(self):
        return f'{self.name}'
