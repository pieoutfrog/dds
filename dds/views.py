from django.utils.dateparse import parse_date
from rest_framework import viewsets, permissions

from dds.models import Category, Subcategory, Type, Transaction
from dds.serializers import TransactionSerializer, CategorySerializer, SubcategorySerializer, TypeSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    """Представление для управления транзакциями."""

    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Transaction.objects.all()

    def get_queryset(self):
        """
        Получаем список транзакций с возможностью фильтрации.

        Параметры фильтрации:
        - status: статус транзакции
        - type: тип транзакции
        - category: категория транзакции
        - subcategory: подкатегория транзакции
        - start_date: начальная дата для фильтрации
        - end_date: конечная дата для фильтрации

        Returns:
            queryset: Отфильтрованный queryset транзакций.
        """
        queryset = super().get_queryset()  # Получаем базовый queryset

        # Получаем параметры фильтрации из запроса
        status = self.request.query_params.get('status', None)
        transaction_type = self.request.query_params.get('type', None)
        category_id = self.request.query_params.get('category', None)
        subcategory_id = self.request.query_params.get('subcategory', None)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)

        # Применяем фильтрацию, если соответствующие параметры переданы
        if status:
            queryset = queryset.filter(status=status)
        if transaction_type:
            queryset = queryset.filter(type_id=transaction_type)  # Используем внешний ключ
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        if subcategory_id:
            queryset = queryset.filter(subcategory_id=subcategory_id)
        if start_date and end_date:
            # Парсинг дат из строки
            start_date_parsed = parse_date(start_date)
            end_date_parsed = parse_date(end_date)
            if start_date_parsed and end_date_parsed:  # Проверяем, что даты валидны
                queryset = queryset.filter(date_created__range=[start_date_parsed, end_date_parsed])

        return queryset

class CategoryViewSet(viewsets.ModelViewSet):
    """Представление для управления категориями."""

    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()

class SubcategoryViewSet(viewsets.ModelViewSet):
    """Представление для управления подкатегориями."""

    serializer_class = SubcategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Subcategory.objects.all()

class TypeViewSet(viewsets.ModelViewSet):
    """Представление для управления типами."""

    serializer_class = TypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Type.objects.all()