# Generated by Django 3.2.8 on 2021-10-11 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_customer_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imageupload',
            old_name='customer_id',
            new_name='customer',
        ),
    ]
