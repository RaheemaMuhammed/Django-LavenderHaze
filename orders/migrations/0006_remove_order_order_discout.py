# Generated by Django 4.1.6 on 2023-03-18 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_order_discout_alter_address_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_discout',
        ),
    ]
