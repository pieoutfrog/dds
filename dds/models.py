from django.db import models
from django.db.models import CASCADE

# Опции для указания, что поле может быть пустым или не заданным
NULLABLE = {'blank': True, 'null': True}


class Type(models.Model):
    """
    Модель, представляющая типы транзакций.

    Attributes:
        name (str): Название типа транзакции.
    """
    name = models.CharField(max_length=50, verbose_name='Тип')
    objects = models.Manager()

    def __str__(self):
        """
        Возвращает строковое представление типа.

        Returns:
            str: Название типа.
        """
        return f'{self.name}'

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Category(models.Model):
    """
    Модель, представляющая категории транзакций.

    Attributes:
        name (str): Название категории.
        type (ForeignKey): Связь с моделью Type.
    """
    name = models.CharField(max_length=50, verbose_name='Имя')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='Тип')
    objects = models.Manager()

    def __str__(self):
        """
        Возвращает строковое представление категории.

        Returns:
            str: Название категории.
        """
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    """
    Модель, представляющая подкатегории категорий транзакций.

    Attributes:
        name (str): Название подкатегории.
        category (ForeignKey): Связь с моделью Category.
    """
    name = models.CharField(max_length=50, verbose_name='Имя')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    objects = models.Manager()

    def __str__(self):
        """
        Возвращает строковое представление подкатегории и связанной категории.

        Returns:
            str: Название подкатегории вместе с категорией.
        """
        return f'{self.name} : {self.category}'

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Status(models.Model):
    """
    Модель, представляющая статус транзакций.

    Attributes:
        name (str): Название статуса транзакции.
    """
    name = models.CharField(max_length=50, verbose_name='Статус')
    objects = models.Manager()

    def __str__(self):
        """
        Возвращает строковое представление статуса.

        Returns:
            str: Название типа.
        """
        return f'{self.name}'

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Transaction(models.Model):
    """
    Модель, представляющая транзакции.

    Attributes:
        STATUS_CHOICES (list): Доступные статусы транзакций.
        date_created (DateField): Дата создания транзакции.
        status (str): Статус транзакции.
        category (ForeignKey): Связь с моделью Category.
        subcategory (ForeignKey): Связь с моделью Subcategory.
        type (ForeignKey): Связь с моделью Type.
        amount (DecimalField): Сумма транзакции.
        comment (TextField): Дополнительный комментарий к транзакции.
    """
    date_created = models.DateField(auto_now_add=True, verbose_name='Дата создания записи')
    status = models.ForeignKey(Status, on_delete=CASCADE, verbose_name='Тип')
    category = models.ForeignKey(Category, on_delete=CASCADE, verbose_name='Категория')
    subcategory = models.ForeignKey(Subcategory, on_delete=CASCADE, verbose_name='Подкатегория')
    type = models.ForeignKey(Type, on_delete=CASCADE, verbose_name='Тип')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')
    comment = models.TextField(**NULLABLE)

    objects = models.Manager()

    def __str__(self):
        """
        Возвращает строковое представление транзакции.

        Returns:
            str: Подробное представление транзакции с суммой, категорией,
                 подкатегорией, статусом, типом, датой создания и комментарием.
        """
        return (f'Транзакция на сумму {self.amount}, '
                f'{self.category}: {self.subcategory}, '
                f'{self.status}, {self.type}, {self.date_created}, '
                f'{self.comment}')

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
