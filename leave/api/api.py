from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from leave.api.serializers import LeaveSerializer, AvailableLeaveSerializer
from utils.utils import get_model


Leave = get_model(app_name="leave", model_name="Leave")
AvailableLeave = get_model(app_name="leave", model_name="AvailableLeave")


class AvailableLeaveViewSet(APIView):
    queryset = AvailableLeave.objects.all()
    serializer_class = AvailableLeaveSerializer

    def get_object(self):
        return self.queryset.get(user=self.request.user)

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_object())
        return Response(serializer.data)


class LeaveViewSet(ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
    search_fields = ["title", "description", "user__username"]
    filterset_fields = ["status"]
