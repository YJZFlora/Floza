# Generated by Django 2.1.5 on 2019-02-19 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_pasta_adding'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='orders',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ManyToManyField(related_name='user', to='orders.User'),
        ),
    ]
