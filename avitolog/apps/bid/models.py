from django.db import models
from datetime import datetime
from avitolog.apps.rk.models import Rk

# Create your models here.
class Client(models.Model):
    fio = models.CharField("ФИО", max_length=63)
    phone = models.CharField("Мобильный", max_length=63)

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

class Executor(models.Model):
    Citys = (
        ("0", "Краснодар"),
        ("1", "Москва")
    )
    city = models.CharField("Город", max_length=2, choices=Citys)
    fio = models.CharField("ФИО", max_length=63)
    phone = models.CharField("Мобильный", max_length=63)

    class Meta:
        verbose_name = 'исполнитель'
        verbose_name_plural = 'исполнители'



class Bid(models.Model):
    rk_id = models.ForeignKey(Rk, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    executor_id = models.ForeignKey(Executor, on_delete=models.CASCADE, verbose_name="Исполнитель")
    datetime = models.DateTimeField("Время создания", default=datetime.today)
    Status = (
        ("0", "Лид"),
        ("1", "Принят"),
        ("2", "Назначен"),
        ("3", "Выполнен"),
        ("4", "Отказ"),
    )
    status = models.CharField("Статус", max_length=2, choices=Status)
    comment = models.TextField("Комментарий", max_length=1023)


    class Meta:
        verbose_name = 'заявка'
        verbose_name_plural = 'заявки'