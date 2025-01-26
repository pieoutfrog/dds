from rest_framework import serializers
from dds.models import Type, Category, Subcategory, Transaction, Status


class TypeSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Type."""

    class Meta:
        model = Type
        fields = ['id', 'name']  # Поля, которые будут сериализоваться


class StatusSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Type."""

    class Meta:
        model = Status
        fields = ['id', 'name']  # Поля, которые будут сериализоваться


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Category."""

    class Meta:
        model = Category
        fields = ['id', 'name', 'type']  # Поля, которые будут сериализоваться


class SubcategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Subcategory."""

    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'category']  # Поля, которые будут сериализоваться


class TransactionSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Transaction."""

    class Meta:
        model = Transaction
        fields = ['id', 'date_created', 'status', 'type', 'category', 'subcategory', 'amount',
                  'comment']  # Поля, которые будут сериализоваться

    def validate(self, data):
        """
        Проверяет данные перед сохранением.

        Validation:
        1. Убедитесь, что подкатегория связана с выбранной категорией.
        2. Убедитесь, что категория связана с выбранным типом.

        Args:
            data (dict): Данные, полученные из запроса.

        Raises:
            serializers.ValidationError: Если валидация не пройдена, будет вызвано исключение.
        """
        # Получаем значения подкатегории, категории и типа из данных
        subcategory = data.get('subcategory')
        category = data.get('category')
        transaction_type = data.get('type')

        # Проверяем наличие подкатегории, связанной с выбранной категорией
        if not Subcategory.objects.filter(id=subcategory.id, category=category).exists():
            raise serializers.ValidationError('Подкатегория не связана с выбранной категорией.')

        # Проверяем наличие категории, связанной с выбранным типом
        if not Category.objects.filter(id=category.id, transaction_type=transaction_type).exists():
            raise serializers.ValidationError('Категория не относится к выбранному типу.')

        return data  # Возвращаем данные, если валидация прошла успешно
