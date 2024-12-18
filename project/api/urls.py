from project.api.api import ProjectViewSet, TaskViewSet, ActivityViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("project", ProjectViewSet, basename="project")
router.register("task", TaskViewSet, basename="task")
router.register("activity", ActivityViewSet, basename="activity")

urlpatterns = router.urls
