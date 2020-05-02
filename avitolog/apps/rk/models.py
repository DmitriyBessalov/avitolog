from django.db import models
from datetime import date

# Create your models here.
class Rk(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Рекламные компания'
        verbose_name_plural = 'Рекламные компании'

class Ad(models.Model):
    rk_id = models.ForeignKey(Rk, on_delete=models.CASCADE, verbose_name="рекламная компания")
    url = models.SlugField(max_length=100)
    create_date = models.DateField("Дата создания", default=date.today)


# class Adisupdate(models.Model):
#     ad_id = models.ForeignKey(Ad, on_delete=models.CASCADE)
