from rest_framework.viewsets import ModelViewSet
from project.api.serializers import ProjectSerializer, TaskSerializer
from utils.utils import get_model

Project = get_model(app_name="project", model_name="Project")
Task = get_model(app_name="project", model_name="Task")


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
