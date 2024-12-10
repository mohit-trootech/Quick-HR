from project.api.api import ProjectViewSet, TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("project", ProjectViewSet, basename="project")
router.register("task", TaskViewSet, basename="task")

urlpatterns = router.urls
