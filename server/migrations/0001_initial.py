# Generated by Django 4.0.1 on 2022-01-27 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_addres', models.GenericIPAddressField(verbose_name='IP-адрес')),
                ('subnet_mask', models.GenericIPAddressField(verbose_name='Маска подсети')),
                ('subnet', models.GenericIPAddressField(verbose_name='Подсеть')),
                ('computer_number', models.IntegerField(verbose_name='Номер компьютера')),
                ('user_name', models.CharField(max_length=255, verbose_name='Ф.И.О. пользователя')),
                ('error', models.CharField(max_length=255, verbose_name='Ф.И.О. пользователя')),
            ],
        ),
    ]