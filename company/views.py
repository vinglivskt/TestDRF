from django.db.models import Count, Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, permissions, generics
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

from company.models import Employee, Department
from company.serializers import EmployeeModelSerializer, DepartmentModelSerializer


# Настройка пагинации
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


# -	API для получения списка сотрудников + реализовать фильтр для поиска по фамилии и по id департамента
# -	Добавление/удаление сотрудников через API
# -	API со списком сотрудников - с пагинацией, API со списком департаментов - без пагинации
# -	Доступ к списку сотрудников - только для авторизованных пользователей, доступ к списку департаментов - доступен и для анонимных пользователей

class EmployeeViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Employee.objects.all()
    filter_backends = [DjangoFilterBackend]
    serializer_class = EmployeeModelSerializer
    filterset_fields = ['last_name', 'department']
    # Изменять данные могут только авторизованные пользователи
    permission_classes = [permissions.IsAuthenticated]
    # Пагинация
    pagination_class = StandardResultsSetPagination
    # Базовая аутентификация использует имя пользователя и пароль для аутентификации.
    # Аутентификация сеанса использует для аутентификации бэкэнд сеанса Django по умолчанию.
    authentication_classes = [SessionAuthentication, BasicAuthentication]


# - API для получения списка департаментов
# (включает искусственное поле с числом сотрудников
# + поле с суммарным окладам по всем сотрудникам)
class DepartmentView(mixins.ListModelMixin, GenericViewSet):
    queryset = Department.objects.annotate(
        employees_count=Count('employees'),
        full_salary=Sum('employees__salary'))
    serializer_class = DepartmentModelSerializer
    # разрешает неограниченный доступ
    permission_classes = [permissions.AllowAny]
