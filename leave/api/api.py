from rest_framework.viewsets import ModelViewSet
from leave.api.serializers import LeaveSerializer
from utils.utils import get_model


Leave = get_model(app_name="leave", model_name="Leave")


class LeaveViewSet(ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
