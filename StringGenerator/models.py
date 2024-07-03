from django.db import models


class Strings(models.Model):
    name = models.CharField("Название - путь", max_length=4000, blank=False)

    class Meta:
        verbose_name = 'Бегущие строки'
        verbose_name_plural = 'Бегущая строка'

    def __str__(self):
        return f'{self.name}'
