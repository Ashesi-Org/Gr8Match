from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from typing import List
from ..serializers import *


@api_view(["POST"])
def create_account(request):
    serializer = CustomUserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        
        if serializer.data["role"] == 'Faculty':
            faculty = Faculty.objects.create(
                account = user,
                project = Projects.objects.filter(id=1).first()
            )
            faculty.save()
        else:
            ra = RA.objects.create(
                availability = 1,
                account = user,
                project = Projects.objects.filter(id=1).first()
            )
            ra.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create accounts for RA or Faculty
@api_view(['POST'])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")
    
    user = authenticate(email=email, password=password)
    if not user:
        return Response({"error": "Invalid credentials!"}, status=status.HTTP_404_NOT_FOUND)
    
    token, created = Token.objects.get_or_create(user=user)
    return Response({"token": token.key}, status=status.HTTP_200_OK)