from rest_framework.viewsets import ModelViewSet
from utils.utils import get_model
from resignation.api.serializers import ResignationSerializer


Resignation = get_model(app_name="resignation", model_name="Resignation")


class ResignationViewSet(ModelViewSet):
    queryset = Resignation.objects.all()
    serializer_class = ResignationSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
