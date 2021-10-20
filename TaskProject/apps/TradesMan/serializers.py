from rest_framework import serializers
from .models import TradeType,TradesMan


class TradeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeType
        fields = ['id','trade_type','status']

class TradesmanSerializer(serializers.ModelSerializer):
    trade_id = TradeTypeSerializer(read_only=True)
    class Meta:
        model = TradesMan
        fields = ('id','trade_man_name','status','trade_id')