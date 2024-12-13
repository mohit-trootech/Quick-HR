from django.urls import path
from organization.api.api import customization_view, organization_view

urlpatterns = [
    path("orgnizations/<str:admin>/", organization_view),
    path("customization/<int:pk>/", customization_view),
]
