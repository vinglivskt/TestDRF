# Generated by Django 3.2.21 on 2023-09-11 08:20

import company.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Департамент',
                'verbose_name_plural': 'Департаменты',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, verbose_name='Имя')),
                ('last_name', models.CharField(db_index=True, max_length=40, verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, max_length=40, verbose_name='Отчество')),
                ('position', models.PositiveSmallIntegerField(choices=[(1, 'Работник'), (2, 'Директор')], verbose_name='Должность')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Оклад')),
                ('photo', models.ImageField(blank=True, upload_to='images/', verbose_name='Фото')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='company.department', verbose_name='Департамент')),
            ],
            options={
                'verbose_name': 'Сотрудника',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='director',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='director', to='company.employee', validators=[company.validators.validate_director], verbose_name='Директор'),
        ),
    ]
