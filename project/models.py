from django.db import models
from django_extensions.db.models import (
    TimeStampedModel,
    TitleDescriptionModel,
    ActivatorModel,
)
from project.constants import VerboseNames, Choices


class Project(TimeStampedModel, TitleDescriptionModel, ActivatorModel):
    deadline = models.DateField(blank=True, null=True)
    project_manager = models.ForeignKey(
        "users.User",
        blank=True,
        related_name=VerboseNames.PROJECT_MANAGER,
        on_delete=models.CASCADE,
        null=True,
    )
    team_lead = models.ForeignKey(
        "users.User",
        blank=True,
        related_name=VerboseNames.TEAM_LEAD,
        on_delete=models.CASCADE,
        null=True,
    )
    assigned_users = models.ManyToManyField(
        "users.User", blank=True, related_name=VerboseNames.ASSIGNED_USERS
    )

    class Meta:
        verbose_name = VerboseNames.PROJECT
        verbose_name_plural = VerboseNames.PROJECT_PLURAL
        unique_together = ("title", "project_manager")

    def __str__(self):
        return self.title

    @property
    def created_at(self):
        from django.utils.timesince import timesince

        return timesince(self.created)


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

    class Meta:
        unique_together = ("title", "project")

    def __str__(self):
        return self.title


class TimeSheet(TimeStampedModel):
    project = models.ForeignKey(
        "project.Project", on_delete=models.CASCADE, related_name=VerboseNames.TIMESHEET
    )
    task = models.ForeignKey(
        "project.Task", on_delete=models.CASCADE, related_name=VerboseNames.TIMESHEET
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name=VerboseNames.TIMESHEET
    )

    class Meta:
        verbose_name = VerboseNames.TIMESHEET_SINGULAR
        verbose_name_plural = VerboseNames.TIMESHEET_PLURAL
        ordering = ("-created",)
