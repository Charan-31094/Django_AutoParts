# Generated by Django 4.2 on 2023-04-30 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orders',
            name='orderid',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
