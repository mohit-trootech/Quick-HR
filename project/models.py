from django.db import models
from django_extensions.db.models import (
    TimeStampedModel,
    TitleDescriptionModel,
    ActivatorModel,
)
from project.constants import VerboseNames, Choices
from django.utils.timesince import timesince
from django_markdown_model.fields import MarkDownField


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
    technologies = models.ManyToManyField(
        "technology.Technology", blank=True, related_name="projects"
    )

    class Meta:
        verbose_name = VerboseNames.PROJECT
        verbose_name_plural = VerboseNames.PROJECT_PLURAL
        unique_together = ("title", "project_manager")

    def __str__(self):
        return self.title

    @property
    def created_ago(self):
        return timesince(self.created)


class Task(TimeStampedModel, TitleDescriptionModel):
    description = MarkDownField(null=True, blank=True)
    project = models.ForeignKey(
        "project.Project", on_delete=models.CASCADE, related_name="tasks"
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


class Activity(TimeStampedModel):
    project = models.ForeignKey(
        "project.Project", on_delete=models.CASCADE, related_name=VerboseNames.ACTIVITY
    )
    task = models.ForeignKey(
        "project.Task", on_delete=models.CASCADE, related_name=VerboseNames.ACTIVITY
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name=VerboseNames.ACTIVITY
    )
    activity_type = models.CharField(
        max_length=16, choices=Choices.TIMER, default=Choices.TIMER_PROGRESS
    )
    duration = models.FloatField(blank=True, null=True, default=0)

    class Meta:
        verbose_name = VerboseNames.ACTIVITY_SINGULAR
        verbose_name_plural = VerboseNames.ACTIVITY_PLURAL
        ordering = ["-created"]

    @property
    def created_ago(self):
        return timesince(self.created)
