from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet, CategoryViewSet, SubcategoryViewSet, TypeViewSet, StatusViewSet

app_name = 'dds'

# Создаем экземпляр маршрутизатора по умолчанию
router = DefaultRouter()

# Регистрируем URL-адреса для каждой из моделей через соответствующие ViewSet'ы
router.register(r'transactions', TransactionViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubcategoryViewSet)
router.register(r'types', TypeViewSet)
router.register(r'status', StatusViewSet)

urlpatterns = [
    # Включаем все зарегистрированные маршруты в urlpatterns
    path('', include(router.urls)),
]