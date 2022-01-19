# Generated by Django 4.0.1 on 2022-01-16 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trains', '0001_initial'),
        ('cities', '0003_alter_city_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название маршрута')),
                ('travel_times', models.PositiveSmallIntegerField(verbose_name='Общее время в пути')),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_from_city_set', to='cities.city', verbose_name='Из какого города')),
                ('to_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_to_city_set', to='cities.city', verbose_name='В какой города')),
                ('trains', models.ManyToManyField(to='trains.Train', verbose_name='Список поездов')),
            ],
            options={
                'verbose_name': 'Маршрут',
                'verbose_name_plural': 'Маршруты',
                'ordering': ['travel_times'],
            },
        ),
    ]
