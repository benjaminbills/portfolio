from rest_framework import generics
from rest_framework import permissions
from portfolio.models import Project
from .serializers import ProjectSerializer
from rest_framework.permissions import BasePermission, IsAdminUser, DjangoModelPermissions, SAFE_METHODS

class ProjectList(generics.ListCreateAPIView):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer
