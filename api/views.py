from rest_framework import generics
from rest_framework.decorators import api_view
from api.email import send_email
from portfolio.models import Project
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from rest_framework import serializers, status
from .serializers import ProjectSerializer
from rest_framework.permissions import BasePermission, IsAdminUser, DjangoModelPermissions, SAFE_METHODS

@api_view(['GET'])
def projectList(request):
  project = Project.objects.all()
  print(project)
  serializer = ProjectSerializer(project, many=True)
  return Response(serializer.data)

@api_view(['POST'])
def SendMail(request):
  data = request.data
  message = data['message']
  name = data['name']
  email = data['email']
  send_email(name, message, email)
  message = {'detail':'successfully saved data'}
  return Response(message,status=status.HTTP_200_OK)