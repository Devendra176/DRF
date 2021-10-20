from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from .serializers import TradeTypeSerializer, TradesmanSerializer
from .models import TradeType, TradesMan
# Create your views here.
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

class TradeTypeView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = TradeType.objects.all()
    serializer_class = TradeTypeSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'trademan/tradelist.html'

    def get(self, request):
        query = TradeType.objects.all()
        serializer = TradeTypeSerializer(query, many=True)
        print(serializer.data)
        return Response({'data':serializer.data})

class TrademanView(APIView):
    permission_classes =  [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'trademan/tradecustomer.html'
    serializer_class = TradesmanSerializer
    
    def get(self, request,pk, tradetype):
        query = TradesMan.objects.filter(trade_id = pk, status=True)
        serializer = TradesmanSerializer(query, many=True)
        print(serializer.data)
        return Response({'data':serializer.data,'trade_type':tradetype})

class AllTradeManView(ListAPIView):
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes =  [IsAuthenticated]
    queryset = TradesMan.objects.all()
    serializer_class = TradesmanSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'trademan/alltradecustomer.html'

    def get(self, request):
        serializer = self.serializer_class(self.get_queryset(),many=True)
        return Response({'data':serializer.data})


