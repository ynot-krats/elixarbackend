# Generated by Django 3.1.1 on 2020-09-21 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalamlabs', '0002_auto_20200921_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kalamregistration',
            name='payment_amount',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
