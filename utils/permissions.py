# Custom Permission Classes
from rest_framework.permissions import IsAuthenticated
from users.constants import Choices


class ManagerPermission(IsAuthenticated):
    def has_permission(self, request, view):
        super().has_permission(request, view)
        if request.user.employee.designation in (Choices.MANAGER):
            return True
        return False
