from cmath import e
from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from Accounts.serializer import Signupserializers, LoginSerializer
from django.contrib.auth.hashers import make_password,check_password
from rest_framework.response import Response
from rest_framework import status




# Create your views here.

user = get_user_model()
@swagger_auto_schema(methods=['POST'], request_body=Signupserializers())
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def signup(request):
    if request.method =="POST":
        serializer = Signupserializers(data =request.data)
        if serializer.is_valid():
            if serializer._validated_data['password'] == serializer._validated_data['re_password']:
                serializer._validated_data['password']=make_password(serializer._validated_data['password'])
                serializer._validated_data['re_password'] = make_password(serializer.validated_data['re_password'])
                User = user.objects.create(**serializer.validated_data)
                serializer_class = Signupserializers(User)
            
                context = {
                        'status': True,
                        'message':'Success',
                        'data': serializer_class.data
                    }
             
                return Response(context, status.HTTP_200_OK)
            
            else:
                context={
                    'status': 'failed',
                    'message': 'Enter a matching password',
                }
                return Response (context, status=status.HTTP_400_BAD_REQUEST)
        else:
            context = {
                'status': False,
                'message':'Failed',
                'error': serializer.errors
            }
            return Response(context, status.HTTP_401_UNAUTHORIZED)
        
@swagger_auto_schema(methods=['POST'], request_body=LoginSerializer())
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])  
def login(request):
    if request.method =='POST':
        user = authenticate(request, username =request.data['username'], password =request.data['password'])
        if user is not None:
            try:
                serializer = Signupserializers(user)
                data ={
                    'status': 'Login success',
                    'data': serializer.data
                }
                return Response(data, status= status.HTTP_202_ACCEPTED)
            except Exception as e:
              raise e
          
          
        else:
              data= {
                  'message': 'please provide a valid username and password',
                  'error': 'This account has not been activated',
              }
              return Response(data, status= status.HTTP_401_UNAUTHORIZED)
        