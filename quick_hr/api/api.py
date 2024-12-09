from rest_framework.viewsets import ModelViewSet
from quick_hr.api.serializers import BroadCastSerializer
from rest_framework.permissions import IsAuthenticated
from utils.utils import get_model

BroadCast = get_model(app_name="quick_hr", model_name="BroadCast")


class BroadCastView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = BroadCast.objects.all()
    serializer_class = BroadCastSerializer
