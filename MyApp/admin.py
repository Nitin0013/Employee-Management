from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Employee, Task

# Register your models here
# from django.contrib import admin


class MyUserAdmin(UserAdmin):
    model = User
    list_display = ("id", "username", "phone_number", "is_staff")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal info",
            {"fields": ("first_name", "last_name", "email", "phone_number")},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )


class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_display = ("id", "user", "employer")


class TaskAdmin(admin.ModelAdmin):
    model = Task
    list_display = (
        "id",
        "title",
        "created_by",
        "assigned_to",
        "status",
        "created_at",
        "updated_at",
    )


admin.site.register(User, MyUserAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Task, TaskAdmin)
