from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView, GenericAPIView
from leave.api.serializers import LeaveSerializer, AvailableLeaveSerializer
from utils.utils import get_model
from users.constants import Choices
from django.utils.timezone import now
from utils.permissions import ManagerPermission
from django.db.models import Q

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
        query = Q(user=self.request.user)
        if (
            self.request.user.employee.designation == Choices.MANAGER
            and self.request.user.employee.department.name == Choices.HR
        ):
            query = query & Q(
                user__employee__organization=self.request.user.employee.organization
            )
        return queryset.filter(query)
