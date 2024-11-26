from django.db import models

class Tovar(models.Model):
    title=models.CharField(max_length=150,verbose_name='Наименование')
    description=models.TextField(verbose_name='Описание')
    image=models.ImageField(upload_to='images',verbose_name='Изображение')
    price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Цена')

    TYPE=[
        ('DO3','Дети до трех лет'),
        ('GRLboy3_6','Девочки и Мальчики 3-6'),
        ('GRLboy7_13','Девочки и Мальчики 7-13'),


    ]
    type=models.CharField(choices=TYPE,max_length=15,default='DO3',verbose_name='Тип')

    def __str__(self):
        return self.title
