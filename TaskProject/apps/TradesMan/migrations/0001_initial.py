# Generated by Django 3.2.8 on 2021-10-06 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookTradeMan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('status', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TradeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_type', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TradesMan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_man_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField()),
                ('status', models.BooleanField(default=False)),
                ('trade_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TradesMan.tradetype')),
            ],
        ),
    ]
