from django.db import models
from django.utils import timezone


class Client(models.Model):

    SEX_CHOICE = (
        ('m', 'Мужской'),
        ('f', 'Женский'),
    )

    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    middle_name = models.CharField('Отчество', max_length=100, blank=True, null=True)
    sex = models.CharField('Пол', choices=SEX_CHOICE, max_length=50)
    birthday = models.DateField('Дата рождения')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['last_name', 'first_name', 'middle_name']

    def __str__(self):
        return '%s %s %s' % (self.last_name, self.first_name, self.middle_name)


class ClientsRequest(models.Model):

    serial_number = models.IntegerField('Номер заявки', unique=True)
    category = models.ForeignKey('ReqCategory')
    create_date = models.DateTimeField('Дата создения', default=timezone.now)
    modify_date = models.DateTimeField('Дата модификации', blank=True, null=True)
    delete_date = models.DateTimeField('Дата удаления', blank=True, null=True)
    client = models.ForeignKey('Client')

    class Meta:
        abstract = True



class LabRequest(ClientsRequest):

    class Meta:
        verbose_name = 'Лабораторная заявка'
        verbose_name_plural = 'Лабораторные заявки'

    def __int__(self):
        return self.serial_number


class MedCenRequest(ClientsRequest):

    req_delivery = models.ForeignKey('Delivery')

    class Meta:
        verbose_name = 'Заявка мед центра'
        verbose_name_plural = 'Заявки мед центра'

    def __int__(self):
        return self.serial_number


class ReqCategory(models.Model):

    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', max_length=240)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Delivery(models.Model):

    DELIV_CHOICE = (
        ('pickup', 'Самовывоз'),
        ('courier', 'Курьером'),
        ('indef', 'Неопределен'),
    )
    address = models.CharField('Адрес', max_length=140)
    delivery_method = models.CharField('Метод доставки', choices=DELIV_CHOICE, max_length=50)
    date_of = models.TimeField('Время выдачи', blank=True, null=True)

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставка'

    def __str__(self):
        return self.address


class XMLClient(Client):

    class Meta:
        proxy = True

    def get_xml(self):
        pass


class PrimeMinister(models.Model):

    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    middle_name = models.CharField('Отчество', max_length=100, blank=True, null=True)
    weight = models.FloatField('Ваш вес')
    email = models.EmailField('E-mail', unique=True)
    salary = models.BigIntegerField('Зарплата', help_text='Пожалуйста, укажите свою реальную зарплату. Так мы сможем решить: сажать или не сажать')
    corrupka = models.BooleanField('Вы коррупционер?', db_column='is_corruption')
    ip = models.GenericIPAddressField(verbose_name='Ваш IP адрес', help_text='Лучше сами введите. Все равно вычислим')


# Create your models here.
