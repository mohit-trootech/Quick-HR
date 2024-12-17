from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView, GenericAPIView
from leave.api.serializers import LeaveSerializer, AvailableLeaveSerializer
from utils.utils import get_model


Leave = get_model(app_name="leave", model_name="Leave")
AvailableLeave = get_model(app_name="leave", model_name="AvailableLeave")


class AvailableLeaveViewSet(RetrieveAPIView, GenericAPIView):
    queryset = AvailableLeave.objects.all()
    serializer_class = AvailableLeaveSerializer

    def get_object(self):
        return self.request.user.available_leave


available_leave = AvailableLeaveViewSet.as_view()


class LeaveViewSet(ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
    search_fields = ["title", "description", "user__username"]
    filterset_fields = ["status"]
