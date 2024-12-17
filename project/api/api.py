from rest_framework.viewsets import ModelViewSet
from project.api.serializers import (
    ProjectSerializer,
    TaskSerializer,
    TimeSheetSerializer,
)
from utils.utils import get_model


Project = get_model(app_name="project", model_name="Project")
Task = get_model(app_name="project", model_name="Task")
TimeSheet = get_model(app_name="project", model_name="TimeSheet")


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_fields = ["status"]
    search_fields = ["title", "description"]


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_fields = ["status", "priority", "assigned_user", "project"]
    search_fields = ["title", "description"]


class TimeSheetViewSet(ModelViewSet):
    queryset = TimeSheet.objects.all()
    serializer_class = TimeSheetSerializer
    filterset_fields = ["project", "task", "user"]
    search_fields = ["project", "task", "user"]
    lookup_field = "user__id"
    lookup_url_kwarg = "pk"

    def get_object(self):
        return TimeSheet.objects.filter(user=self.request.user).first()
