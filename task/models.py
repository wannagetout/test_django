from datetime import date

from django.db import models


class Tasks(models.Model):
    """
    Модель задачи
    """
    description = models.TextField(verbose_name='Описание задачи', null=False)
    status = models.BooleanField(verbose_name='Статус задачи', default=True)
    create_date = models.DateField(verbose_name='Дата создания', default=date.today())
    update_date = models.DateField(verbose_name='Дата изменения', default=date.today())

    def __str__(self) -> str:
        return f'{self.description}, {self.status}, {self.create_date}'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ('status',)
