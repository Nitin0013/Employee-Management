from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import User, Employee, Task
from .serializers import UserSerializer, EmployeeSerializer, TaskSerializer

# Create your views here.
# from django.shortcuts import render


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset
        elif self.request.user.is_authenticated and self.request.user.employee:
            return self.queryset.filter(employer=self.request.user)
        else:
            return Employee.objects.none()


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset
        elif self.request.user.is_authenticated and self.request.user.employee:
            return self.queryset.filter(assigned_to=self.request.user.employee)
        else:
            return Task.objects.none()
