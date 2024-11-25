from rest_framework.viewsets import ModelViewSet
from overtime.api.serializers import OvertimeSerializer
from utils.utils import get_model

Overtime = get_model(app_name="overtime", model_name="Overtime")


class OvertimeViewSet(ModelViewSet):
    queryset = Overtime.objects.all()
    serializer_class = OvertimeSerializer
