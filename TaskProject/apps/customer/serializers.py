# from .models import User
import datetime
from django.contrib.auth import get_user, get_user_model

from django.http import request
# from django.contrib.auth import authenticate, login
from .models import Customer, ImageUpload
# from django.conf import settings
from rest_framework import serializers

class Usersializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
        extra_fields ={'password':{'write_only':True},}


class LoginSerializer(serializers.Serializer):
    username= serializers.CharField(max_length=10)

    def create(self,validated_data,**kwargs):
        user = get_user_model().objects.filter(username=validated_data['username'])
        
        if user.exists()==False:
            get_user_model().objects.create_user(username=validated_data['username'], password=str(kwargs['context']['otp']))
        else:
            user = get_user_model().objects.get(username=validated_data['username'])
            user.set_password(str(kwargs['context']['otp']))
            user.save()
        return user
    
    def validate(self,data):
        username = data.get('username',None)
        if username == None:
            raise serializers.ValidationError("Phone no. cant be empty")
        else:
            pass
        return data

def gettime():
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    return int(now)
def converttime(stringtime):
    stringtime =stringtime.strftime("%Y%m%d%H%M%S")

    return int(stringtime)


class OtpVerificationSerializer(serializers.Serializer):
    Otp = serializers.CharField(max_length=50)
    def validate(self,validated_data,*args,**kwargs):
        otp = validated_data.get('Otp',None)
        print(otp)
        print(self.context)
        print(get_user_model().objects.filter(username=self.context['phone']))
        querydata = get_user_model().objects.get(username=self.context['phone'])
        print(querydata)
        if otp == None or otp == '':
            raise serializers.ValidationError("OTP cant be empty")

        elif (querydata.check_password(str(otp)) == False) or gettime() > converttime(querydata.expiry_date):
            # print( gettime() > converttime(querydata.expiry_date),querydata.check_password(str(otp)) == False)
            raise serializers.ValidationError("OTP has been expired")

        return validated_data

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def filer(self,email):
        return Customer.objects.filter(email_address=email)


class CustomerProfileSerializer(serializers.Serializer):

    customer_name  =serializers.CharField(max_length=150)
    email_address = serializers.CharField(max_length=255)
    date_of_birth =serializers.DateField()

    # def create(self,validated_data,*args,**kwargs):
    #     customer_name = validated_data.get('customer_name',None)
    #     email_address = validated_data.get('email_address',None)
    #     date_of_birth = validated_data.get('date_of_birth',None)
    #     user  = CustomerSerializer().filer(email=email_address)
    #     if not user:
    #         print(kwargs['context']['phone'])
    #         user = Customer.objects.create(customer_name=customer_name,email_address=email_address,date_of_birth=date_of_birth,mobile_number=kwargs['context']['phone'])
    #     return validated_data

    def validate(self,validated_data):
        customer_name = validated_data.get('customer_name',None)
        email_address = validated_data.get('email_address',None)
        date_of_birth = validated_data.get('date_of_birth',None)
        if customer_name==None or email_address==None or customer_name=='' or email_address=='' or date_of_birth==None:
            raise serializers.ValidationError("field required")
        return validated_data

class ProfilePicturSerializer(serializers.ModelSerializer):
    customer_id = serializers.IntegerField(source='customer.id')
    
    class Meta:
        model = ImageUpload
        fields = '__all__'
    
    def validate(self, validated_data):
        customer_id = validated_data.get('customer_id', None)
        if customer_id != None:
            customer_id = int(customer_id)
    



