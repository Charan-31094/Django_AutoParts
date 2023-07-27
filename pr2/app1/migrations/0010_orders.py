# Generated by Django 4.2 on 2023-04-25 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_alter_registration_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=40)),
                ('orderid', models.CharField(max_length=50)),
                ('product_id', models.IntegerField()),
                ('ordered_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'orders_table',
            },
        ),
    ]
