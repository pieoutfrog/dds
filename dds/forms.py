from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    """
    Форма для создания и редактирования транзакций.

    Attributes:
        Meta (class): Настройки формы, определяющие связанную модель
        и поля, которые нужно использовать.
    """
    class Meta:
        model = Transaction  # Связь с моделью Transaction
        fields = '__all__'  # Использовать все поля модели (или перечислите их вручную)

    def clean(self):
        """
        Проверка валидности вводимых данных.

        Проверяет, что обязательные поля заполнены и что
        отношения между выбранными категорией и подкатегорией
        соответствуют правилам.

        Raises:
            ValidationError: Если какие-либо проверки не прошли,
            ошибки будут добавлены к форме.
        """
        cleaned_data = super().clean()  # Получаем очищенные данные из суперкласса
        amount = cleaned_data.get('amount')
        type = cleaned_data.get('type')
        category = cleaned_data.get('category')
        subcategory = cleaned_data.get('subcategory')

        # Проверка обязательных полей
        if not amount:
            self.add_error('amount', 'Поле "Сумма" обязательно для заполнения.')
        if not type:
            self.add_error('type', 'Поле "Тип" обязательно для заполнения.')
        if not category:
            self.add_error('category', 'Поле "Категория" обязательно для заполнения.')
        if not subcategory:
            self.add_error('subcategory', 'Поле "Подкатегория" обязательно для заполнения.')

        # Проверка зависимости подкатегории от категории
        if subcategory and category and subcategory.category != category:
            self.add_error('subcategory', 'Выбранная подкатегория не связана с выбранной категорией.')

        # Проверка зависимости категории от типа
        if category and type and category.type != type:
            self.add_error('category', 'Выбранная категория не относится к выбранному типу.')