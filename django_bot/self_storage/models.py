from django.db import models


# TODO: пользователь регается, и в своем ЛК можешь в любой момент вызвать курьера, например.
class Client(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    tg_id = models.BigIntegerField(unique=True)
    address = models.CharField(max_length=50)  # для курьера


# TODO: qr код должен быть уникальным для каждой посылки у каждого пользователя, т.к. посылок может быть несколько.
#      Можно сделать поле с рандомным числом, и при запросе оно накладывается на картинку - шаблон.
#      Добавить функцию отсчета дней
class Order(models.Model):
    days = models.IntegerField(max_length=10)
    size = models.CharField(max_length=12)
    delivery = models.CharField(max_length=12)  # TODO нужна ли доставка/замер, использовать в админке для развозки
    days_left = models.CharField(max_length=12)  # TODO остаток дней до конца аренды (возможно лишнее, подумать)
    key_of_cell = models.IntegerField(max_length=10)


# TODO: у каждого склада будет своя вместительность, когда пользователь выберет сколько нужно места, то список складов
#       отфильтруется, и покажет доступные. Если доступных нету, или пользователю неудобно отвезти на нужный склад,
#       вывести на экран "уменьшите объем посылки и тп."
class Warehouse(models.Model):
    address = models.CharField(max_length=30)
    free_capacity = models.IntegerField(max_length=30)

    # TODO тарифы на хранение, наверное, лишнее, подумать


class Plans(models.Model):
    pass
