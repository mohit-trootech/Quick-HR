from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from quick_hr.api.urls import router as api_router

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("users.urls", namespace="users")),
    path("api/", include(api_router.urls)),
    path("api/attendence/", include("attendence.urls", namespace="attendence")),
    path("api/devices/", include("device.urls", namespace="device")),
    path("api/leaves/", include("leave.urls", namespace="leave")),
    path("api/overtime/", include("overtime.urls", namespace="overtime")),
    path("api/projects/", include("project.urls", namespace="project")),
    path("api/reviews/", include("review.urls", namespace="review")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)
