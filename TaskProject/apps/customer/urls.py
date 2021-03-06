from django.urls import path, include
from rest_framework import routers, views
from . import views as func_views
from .views import (UserViewSet, UserCreatePhoneView, OtpVerification, CustomerProfile, CustomerProfilePictureUpload,)

# router =  routers.DefaultRouter()
# router.register(r'',UserViewSet)
app_name = 'customer'
urlpatterns = [
    # path('',include(router.urls)),
    path('', UserCreatePhoneView.as_view(),name='login'),
    path('otp/<str:phone>/', OtpVerification.as_view(),name="otp_verification"),
    path('<str:phone>/customer/',CustomerProfile.as_view(),name="customer_profile"),
    path('<str:phone>/customer/profile/',CustomerProfilePictureUpload.as_view(),name="customer_profilepic"),
    path('logout/',func_views.logout_view,name="logout"),
]