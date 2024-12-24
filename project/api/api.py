from rest_framework.viewsets import ModelViewSet
from project.api.serializers import (
    ProjectSerializer,
    TaskSerializer,
    ActivitySerializer,
)
from utils.utils import get_model
from django_extensions.db.models import ActivatorModel
from project.constants import Choices
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.timezone import now
from rest_framework.status import HTTP_200_OK
from rest_framework.pagination import PageNumberPagination

Project = get_model(app_name="project", model_name="Project")
Task = get_model(app_name="project", model_name="Task")
Activity = get_model(app_name="project", model_name="Activity")


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.filter(status=ActivatorModel.ACTIVE_STATUS)
    serializer_class = ProjectSerializer
    filterset_fields = ["status"]
    search_fields = ["title", "description"]
    pagination_class = PageNumberPagination

    @action(detail=False, methods=["get"])
    def list_users_assigned_projects(self, request, *args, **kwargs):
        filtered_queryset = self.queryset.filter(
            assigned_users__id=self.request.user.id
        ).distinct()

        paginator = self.pagination_class()
        page = paginator.paginate_queryset(filtered_queryset, request)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = self.get_serializer(filtered_queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.filter(status=Choices.OPEN)
    serializer_class = TaskSerializer
    filterset_fields = ["status", "priority", "project"]
    search_fields = ["title", "description"]

    def filter_queryset(self, queryset):
        if self.request.query_params.get("project"):
            return self.queryset.filter(
                project__id=self.request.query_params.get("project")
            )
        return super().filter_queryset(queryset)


class ActivityViewSet(ModelViewSet):
    queryset = Activity.objects.filter(created__year=now().year)
    serializer_class = ActivitySerializer
    filterset_fields = ["activity_type", "task", "user", "project"]
    search_fields = ["activity_type"]
    ordering = ["-created"]
    permission_classes = []

    @action(detail=False, methods=["get"])
    def last_user_activity(self, request, *args, **kwargs):
        filtered_queryset = self.filter_queryset(self.get_queryset())
        last_activity = (
            filtered_queryset.filter(
                activity_type__in=[
                    Choices.TIMER_START,
                    Choices.TIMER_PAUSE,
                    Choices.TIMER_PROGRESS,
                ],
                user=self.request.user,
            )
            .order_by("-created")
            .first()
        )

        if last_activity is None:
            return Response(status=HTTP_200_OK)
        serializer = self.get_serializer(last_activity)

        return Response(serializer.data, status=HTTP_200_OK)
