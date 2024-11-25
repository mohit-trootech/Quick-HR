from project.api.api import ProjectViewSet, TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", ProjectViewSet, basename="project")
router.register("", TaskViewSet, basename="task")

urlpatterns = router.urls
