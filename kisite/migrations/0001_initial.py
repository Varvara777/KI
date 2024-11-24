# Generated by Django 5.1.3 on 2024-11-24 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tovar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='images', verbose_name='Изображение')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('type', models.CharField(choices=[('DO3', 'Дети до трех лет'), ('GRL3_6', 'Девочки 3-6'), ('BOY3_6', 'Мальчики 3-6'), ('GRL7_13', 'Девочки 7-13'), ('GRL7_13', 'Девочки 7-13'), ('ForParents', 'Настолки для мам и пап')], default='DO3', max_length=15, verbose_name='Тип')),
            ],
        ),
    ]