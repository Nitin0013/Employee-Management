from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
# from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name="groups",
        blank=True,
        help_text=(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name="myapp_users",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="user permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="myapp_users",
        related_query_name="user",
    )


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee")
    employer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="employees"
    )


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_tasks"
    )
    assigned_to = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="assigned_tasks"
    )
    status = models.CharField(
        max_length=20,
        choices=(
            ("Not Started", "Not Started"),
            ("Started", "Started"),
            ("Finished", "Finished"),
            ("Blocked", "Blocked"),
        ),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
