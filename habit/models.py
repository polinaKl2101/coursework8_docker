from django.db import models
from config import settings
from users.models import NULLABLE


class Habit(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    place = models.CharField(max_length=50, verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    action = models.CharField(max_length=155, verbose_name='Действие')
    pleasant_habit = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    linked_habit = models.ForeignKey('Habit', on_delete=models.SET_NULL, null=True, verbose_name='Связанная привычка')
    periodicity = models.IntegerField(default=1, verbose_name='Периодичность')
    reward = models.CharField(max_length=155, verbose_name='Вознаграждение', **NULLABLE)
    execution_time = models.IntegerField(verbose_name='Время на выполнение')
    public = models.BooleanField(default=False, verbose_name='Признак публичности')

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
