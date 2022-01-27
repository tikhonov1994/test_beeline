from django.db import models


class Data(models.Model):
    ip_addres = models.GenericIPAddressField(verbose_name='IP-адрес')
    subnet_mask = models.GenericIPAddressField(verbose_name='Маска подсети')
    subnet = models.GenericIPAddressField(verbose_name='Подсеть',
                                          null=True, blank=True)
    computer_number = models.IntegerField(verbose_name='Номер компьютера')
    user_name = models.CharField(max_length=255,
                                 verbose_name='Ф.И.О. пользователя')
    error = models.CharField(max_length=255,
                             verbose_name='Ошибка',
                             null=True, blank=True)
