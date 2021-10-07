from django.db import models
from apps.customer.models import Customer
# Create your models here.
class Choice():
    PENDDING = 0
    BOOKED = 1
    CANCEL = -1

class TradeType(models.Model):
    trade_type = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.trade_type

class TradesMan(models.Model):
    trade_id = models.ForeignKey(TradeType,on_delete=models.CASCADE)
    trade_man_name = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.trade_man_name

class BookTradeMan(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    trade_man = models.ForeignKey(TradesMan,on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    status = models.SmallIntegerField(default=Choice.PENDDING)

    def __str__(self):
        return "BookTradeMan Customer:" % self.customer