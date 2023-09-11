from rest_framework.routers import DefaultRouter

from company.views import EmployeeViewSet, DepartmentView

# Создаем наборы маршрутов с router
# Маршрутизация ресурсов позволяет быстро объявить все общие маршруты для данного ресурсного контроллера

router = DefaultRouter()
router.register(r'employee', EmployeeViewSet, basename='employee')
router.register(r'department', DepartmentView, basename='department')
urlpatterns = router.urls
