from django.contrib import admin

from dds.forms import TransactionForm
from dds.models import Category, Subcategory, Transaction, Type, Status


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Указанные поля, отображаемые в списке категорий
    list_filter = (
        'name',  # Возможность фильтрации по имени
        'type',  # Фильтрация по типу
    )


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')  # Указанные поля, отображаемые в списке подкатегорий
    list_filter = (
        'name',  # Возможность фильтрации по имени
        'category',  # Фильтрация по категории
    )


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_created', 'status', 'type', 'category',
                    'subcategory', 'amount', 'comment')  # Указанные поля для отображения
    list_filter = (
        'status',  # Фильтрация по статусу
        'type',  # Фильтрация по типу
        'category',  # Фильтрация по категории
        'subcategory',  # Фильтрация по подкатегории
        'date_created',  # Дата создания (позволяет фильтровать по дате)
    )
    date_hierarchy = 'date_created'  # Добавляет навигацию по датам в админке
    form = TransactionForm  # Использование пользовательской формы для валидации


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Указанные поля для отображения типов


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Указанные поля для отображения типов
