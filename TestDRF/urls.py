from django.contrib import admin

from django.urls import path, include, re_path

from .yaysg import urlpatterns as doc_urls
from django.views.generic.base import TemplateView

urlpatterns = [
    # начальная страница
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    # админка django
    path('admin/',
         admin.site.urls),
    # авторизация на основе сессии. Добавит Login и Logout
    path('api-auth/',
         include('rest_framework.urls')),
    # Набор API методов для работы с данными по сотрудникам и департаментам
    path('api/', include('company.urls')),

]

urlpatterns += doc_urls
