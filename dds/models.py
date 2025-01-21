from django.db import models
from django.db.models import CASCADE

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория')
    object = models.Manager()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Подкатегория')
    objects = models.Manager()

    def __str__(self):
        return f'{self.name} : {self.category}'

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Transaction(models.Model):
    STATUS_CHOICES = [
        ('business', 'Бизнес'),
        ('personal', 'Личное'),
        ('tax', 'Налог'),
    ]

    TYPE_CHOICES = [
        ('income', 'Пополнение'),
        ('expense', 'Списание'),
    ]
    date_created = models.DateField(auto_now_add=True, verbose_name='Дата создания записи')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='private', verbose_name='Статус')
    type = models.CharField(max_length=15, choices=TYPE_CHOICES, default='expense', verbose_name='Тип')
    category = models.ForeignKey(Category, on_delete=CASCADE, verbose_name='Категория')
    subcategory = models.ForeignKey(Subcategory, on_delete=CASCADE, verbose_name='Подкатегория')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(**NULLABLE)
    objects = models.Manager()

    def __str__(self):
        return (f'Транзакция на сумму  {self.amount}'
                f'{self.category}:{self.subcategory},'
                f'{self.status}, {self.type}, {self.date_created},'
                f'{self.comment}')

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
