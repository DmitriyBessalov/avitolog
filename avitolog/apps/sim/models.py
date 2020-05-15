from django.db import models

# Create your models here.
class Sim(models.Model):
    # Citys = (
    #     ("0", "Краснодар"),
    #     ("1", "Москва")
    # )
    # city = models.CharField("Город", max_length=2, choices=Citys)
    # fio = models.CharField("ФИО", max_length=63)
    # phone = models.CharField("Мобильный", max_length=63)
    Provider = (
        ("0", "Ростелеком"),
        ("1", "Теле2"),
        ("2", "Билайн"),
        ("3", "Мегафон"),
        ("4", "МТС")
    )
    provider = models.CharField("Провайдер", max_length=1, choices=Provider)
    tarif = models.CharField("Тариф", max_length=31)
    balans = models.FloatField("Баланс")
    last_balans_check = models.DateField("Дата просмотра баланса")
    last_pay_action = models.DateField("Дата последнего платного действия")

    class Meta:
        verbose_name = 'симка'
        verbose_name_plural = 'симки'

