from django.urls import path, include
from rest_framework import routers
from .views import TradeTypeView, TrademanView, AllTradeManView

# router =  routers.DefaultRouter()
app_name = 'Tradesman'
urlpatterns = [
    path('tradelist/',TradeTypeView.as_view(),name='tradelist'),
    path('<int:pk>/<str:tradetype>/trademan/',TrademanView.as_view(),name='tademan'),
    path('alltrademan/',AllTradeManView.as_view(),name='trademanlist'),
    
]