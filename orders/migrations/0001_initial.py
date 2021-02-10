# Generated by Django 2.1.5 on 2019-01-26 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Basic_size', models.CharField(max_length=64)),
                ('Topping', models.CharField(max_length=64)),
                ('Sub', models.CharField(max_length=64)),
                ('Salad', models.CharField(max_length=64)),
                ('Beverage', models.CharField(max_length=64)),
                ('Pasta', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('Notes', models.CharField(max_length=500)),
                ('Basic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basic', to='orders.Items')),
                ('Beverage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beverage', to='orders.Items')),
                ('Pasta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pasta', to='orders.Items')),
                ('Salad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salad', to='orders.Items')),
                ('Sub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub', to='orders.Items')),
                ('Topping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topping', to='orders.Items')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('orders', models.ManyToManyField(blank=True, related_name='users', to='orders.Order')),
            ],
        ),
    ]
