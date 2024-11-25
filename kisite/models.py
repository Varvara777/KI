from django.db import models

class Tovar(models.Model):
    title=models.CharField(max_length=150,verbose_name='Наименование')
    description=models.TextField(verbose_name='Описание')
    image=models.ImageField(upload_to='images',verbose_name='Изображение')
    price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Цена')

    TYPE=[
        ('DO3','Дети до трех лет'),
        ('GRL3_6','Девочки 3-6'),
        ('BOY3_6','Мальчики 3-6'),
        ('GRL7_13','Девочки 7-13'),
        ('GRL7_13','Мальчики 7-13'),
        ('ForParents','Настолки для мам и пап')

    ]
    type=models.CharField(choices=TYPE,max_length=15,default='DO3',verbose_name='Тип')

    def __str__(self):
        return self.title
