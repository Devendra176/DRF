from django.contrib import admin
from .models import TradeType, TradesMan, BookTradeMan
# Register your models here.
admin.site.register(TradeType)
admin.site.register(TradesMan)
admin.site.register(BookTradeMan)
