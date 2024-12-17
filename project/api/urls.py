from project.api.api import ProjectViewSet, TaskViewSet, TimeSheetViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("project", ProjectViewSet, basename="project")
router.register("task", TaskViewSet, basename="task")
router.register("timesheet", TimeSheetViewSet, basename="timesheet")

urlpatterns = router.urls
