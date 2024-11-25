from django.db import models
from django_extensions.db.models import (
    TimeStampedModel,
    TitleDescriptionModel,
    ActivatorModel,
)
from project.constants import VerboseNames, Choices


class Project(TimeStampedModel, TitleDescriptionModel, ActivatorModel):
    project_manager = models.ManyToManyField(
        "users.User", blank=True, related_name=VerboseNames.PROJECT_MANAGER
    )
    team_lead = models.ManyToManyField(
        "users.User", blank=True, related_name=VerboseNames.TEAM_LEAD
    )
    assigned_users = models.ManyToManyField(
        "users.User", blank=True, related_name=VerboseNames.ASSIGNED_USERS
    )


class Task(TimeStampedModel, TitleDescriptionModel):
    project = models.ForeignKey("project.Project", on_delete=models.CASCADE)
    assigned_user = models.ForeignKey(
        "users.User", on_delete=models.SET_NULL, null=True
    )
    status = models.CharField(
        max_length=16, choices=Choices.STATUS, default=Choices.OPEN
    )
    priority = models.CharField(
        max_length=16, choices=Choices.PRIORITY, default=Choices.LOW
    )
