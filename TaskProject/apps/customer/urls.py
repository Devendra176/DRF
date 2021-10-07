from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, UserCreatePhoneView, OtpVerification, CustomerProfile, CustomerProfilePictureUpload

# router =  routers.DefaultRouter()
# router.register(r'',UserViewSet)
app_name = 'customer'
urlpatterns = [
    # path('',include(router.urls)),
    path('', UserCreatePhoneView.as_view(),name='login'),
    path('otp/', OtpVerification.as_view(),name="otp_verification"),
    path('customer/',CustomerProfile.as_view(),name="customer_profile"),
    path('customer/profile/',CustomerProfilePictureUpload.as_view(),name="customer_profilepic"),
]