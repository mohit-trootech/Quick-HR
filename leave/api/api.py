from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin
from leave.api.serializers import LeaveSerializer, AvailableLeaveSerializer
from utils.utils import get_model
from rest_framework.permissions import IsAuthenticated


Leave = get_model(app_name="leave", model_name="Leave")
AvailableLeave = get_model(app_name="leave", model_name="AvailableLeave")


class AvailableLeaveViewSet(ListModelMixin, GenericViewSet):
    queryset = AvailableLeave.objects.all()
    serializer_class = AvailableLeaveSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class LeaveViewSet(ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
