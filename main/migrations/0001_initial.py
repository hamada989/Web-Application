# Generated by Django 3.2.4 on 2021-06-16 18:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BasketGenre', models.CharField(max_length=200)),
                ('BasketSlug', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Baskets',
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 6, 16, 14, 40, 19, 703768), verbose_name='date created')),
                ('film_slug', models.CharField(default=1, max_length=200)),
                ('BasketGenre', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.basket', verbose_name='basket')),
            ],
        ),
    ]
