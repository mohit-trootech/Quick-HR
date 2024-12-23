# Custom Permission Classes
from rest_framework.permissions import IsAuthenticated
from users.constants import Choices


class ManagerPermission(IsAuthenticated):
    def has_permission(self, request, view):
        permission = super().has_permission(request, view)
        return all([permission, request.user.employee.designation in (Choices.MANAGER)])


class DepartmentManager(IsAuthenticated):
    def has_permission(self, request, view):
        permission = super().has_permission(request, view)
        return all([permission, request.user.employee.designation == Choices.MANAGER])
