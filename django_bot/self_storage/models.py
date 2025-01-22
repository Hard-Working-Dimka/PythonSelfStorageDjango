from django.db import models
import random


def generate_cell_key():
    return random.randrange(100, 10000)


# TODO: пользователь регается, и в своем ЛК можешь в любой момент вызвать курьера, например.
class Client(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    tg_id = models.BigIntegerField(unique=True)
    address_of_client = models.CharField(max_length=50)  # для курьера


# TODO: у каждого склада будет своя вместительность, когда пользователь выберет сколько нужно места, то список складов
#       отфильтруется, и покажет доступные. Если доступных нету, или пользователю неудобно отвезти на нужный склад,
#       вывести на экран "уменьшите объем посылки и тп."
class Warehouse(models.Model):
    address = models.CharField(max_length=30)
    free_capacity = models.IntegerField()


# TODO тарифы на хранение, наверное, лишнее, подумать
class Plans(models.Model):
    price = models.IntegerField()
    volume_of_cell = models.IntegerField()


# TODO: qr код должен быть уникальным для каждой посылки у каждого пользователя, т.к. посылок может быть несколько.
#      Можно сделать поле с рандомным числом, и при запросе оно накладывается на картинку - шаблон.
#      Добавить функцию отсчета дней
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    cell_address = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plans, on_delete=models.CASCADE)

    days = models.IntegerField()
    size = models.CharField(max_length=12)
    delivery = models.BooleanField(max_length=12)  # TODO нужна ли доставка/замер, использовать в админке для развозки
    days_left = models.CharField(max_length=12)  # TODO остаток дней до конца аренды (возможно лишнее, подумать)
    key_of_cell = models.IntegerField(editable=False, default=generate_cell_key())
    items = models.CharField(max_length=256)  # описание (что хранится)
