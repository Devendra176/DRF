from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from django.http.response import  JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from random import randint
# from rest_framework import serializers
from rest_framework.serializers import Serializer
from twilio.base import serialize
from twilio.rest import Client
from .models import Customer, ImageUpload
# Create your views here.
from django.contrib.auth import authenticate, get_user_model,login, get_user,logout
from rest_framework.authentication import SessionAuthentication
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
# from rest_framework import permissions
from .serializers import Usersializer, LoginSerializer, OtpVerificationSerializer, CustomerProfileSerializer,ProfilePicturSerializer, CustomerSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = get_user_model().objects.all().order_by('-date_joined')
    serializer_class = Usersializer
    # permission_classes = [permissions.IsAuthenticated]

def OTPGenerate(phone):
    try:
        account_sid= settings.YOUR_ACCOUNT_SID
        auth_token = settings.YOUR_AUTH_TOKEN
        trail_num = settings.YOUR_TRAIL_NUMBER
        otp =  randint(100000, 999999)
        client = Client(account_sid, auth_token)
        to = '+91'+phone
        message = client.messages.create(
                                            body=f'Hi, your OTP  is {otp} ', from_=trail_num, to=to
                                        )
        print(message.sid)
    except Exception as e:
        print(e)
    return otp


class UserCreatePhoneView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'customers/login.html'
    def get(self, request):
        content = {'message':'hello'}
        return Response(content)

    def post(self, request,*args, **kwargs):
        phone = request.data.get('username',None)
        # request.session['phone'] = phone
        # otp = OTPGenerate(phone)
        otp=123456
        # print(request.session.get('phone'))
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            LoginSerializer().create(serializer.data,context={'otp': otp})
            return JsonResponse({'status':1003,'message':'Verification OTP sent on a mobile number','url':'otp/{}/'.format(phone)})
        return JsonResponse({'message':status.HTTP_400_BAD_REQUEST})
    
class OtpVerification(APIView):
    permission_classes = [AllowAny]
    serializer_class = OtpVerificationSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'customers/otp.html'

    def get(self, request, phone):
        content={'message':'enter otp','phone':phone}
        return Response(content)

    def post(self, request,phone):
        serializer = OtpVerificationSerializer(data=request.data,context={'phone':phone})
        if serializer.is_valid():
            print(request.data)
            user = authenticate(request,username=phone,password=request.data.get('Otp'))
            login(request, user)
            refresh =  RefreshToken.for_user(user)
            return JsonResponse({'status':1001,'message':'Verify','payload':serializer.data,'refresh':str(refresh),'access':str(refresh.access_token),'url':'/api/customer/{}/customer/'.format(phone)})
        return JsonResponse({'status':400,'message':'error'})

class CustomerProfile(APIView):
    authentication_classes =[JWTAuthentication,SessionAuthentication]
    permission_classes = [AllowAny]
    serializer_class = CustomerSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'customers/customerprofilepic.html'

    def get(self, request, phone):
        query = Customer.objects.filter(mobile_number=phone).exists()
        imagedata=None
        if query:
            query = Customer.objects.get(mobile_number=phone)
            image = ImageUpload.objects.filter(customer_id=query.id)
            if image.exists():
                imagedata=ProfilePicturSerializer(ImageUpload.objects.get(customer_id=query.id))
                imagedata=imagedata.data
            serializer=CustomerSerializer(query)
            data = serializer.data
            return Response({'phone':phone,'message':'fill details','status':100,'data':data,'imagedata':imagedata})
        return Response({'status':400,'message':'No data found','phone':phone})

    def post(self, request,phone):
        serializer = CustomerSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':1001,'message':'Verify'})
        return JsonResponse({'status':400,'message':'error'})

class CustomerProfilePictureUpload(CreateAPIView):
    authentication_classes =[JWTAuthentication]
    permission_classes = [AllowAny]
    serializer_class = ProfilePicturSerializer
    def post(self, request,phone):
        print(request.data)
        serializer = ProfilePicturSerializer(data=request.data)
        print(serializer.is_valid())
        # print(request.data.get('imagepath'))
        pass
        # if serializer.is_valid():
        #     pass
        # return Response(serializer.data)




def logout_view(request):
    logout(request)
    return Response({'message':'user logged out'})
        

        
         
        

