from django.db import models


# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=50, verbose_name='商品名')
    price = models.IntegerField(verbose_name='価格')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'items'
        verbose_name = verbose_name_plural = '販売商品'
