from django.contrib.admin import ModelAdmin, register
from utils.utils import get_model


Review = get_model(app_name="review", model_name="Review")


@register(Review)
class ReviewAdmin(ModelAdmin):
    list_display = (
        "month",
        "reviewer",
        "reviewee",
        "performance_rating",
        "delivery_rating",
        "socialization_rating",
        "created",
    )
    list_filter = ("month", "reviewer", "reviewee", "created")
    search_fields = ("reviewer__username", "reviewee__username")
    readonly_fields = ("created", "modified")
    ordering = ("-created",)
