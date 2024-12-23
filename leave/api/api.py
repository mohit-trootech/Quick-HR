from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView, GenericAPIView
from leave.api.serializers import LeaveSerializer, AvailableLeaveSerializer
from utils.utils import get_model
from users.constants import Choices
from django.utils.timezone import now
from utils.permissions import ManagerPermission

Leave = get_model(app_name="leave", model_name="Leave")
AvailableLeave = get_model(app_name="leave", model_name="AvailableLeave")
Department = get_model(app_name="users", model_name="Department")


class AvailableLeaveViewSet(RetrieveAPIView, GenericAPIView):
    queryset = AvailableLeave.objects.all()
    serializer_class = AvailableLeaveSerializer

    def get_object(self):
        return self.request.user.available_leave


available_leave = AvailableLeaveViewSet.as_view()


class LeaveViewSet(ModelViewSet):
    queryset = Leave.objects.filter(end_date__gte=now())
    serializer_class = LeaveSerializer
    search_fields = ["title", "description"]
    filterset_fields = ["status"]

    def get_permissions(self):
        if self.request.method in ("PUT", "PATCH"):
            return [ManagerPermission()]
        return super().get_permissions()

    def filter_queryset(self, queryset):
        if (
            self.request.user.employee.designation == Choices.MANAGER
            and self.request.user.employee.department.name == Choices.HR
        ):
            return self.queryset.filter(
                user__employee__organization=self.request.user.employee.organization,
            )
        return super().filter_queryset(user=self.request.user)
