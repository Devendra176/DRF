from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.views import APIView
# from rest_framework import permissions
from .serializers import UserCreateSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = get_user_model().objects.all().order_by('-date_joined')
    serializer_class = UserCreateSerializer
    # permission_classes = [permissions.IsAuthenticated]

class UserCreateView(APIView):
    def get(self, request):
        content = {'message':'hello'}
        return Response(content)
    def post(self, request):

