from django.contrib.admin import ModelAdmin, register
from utils.utils import get_model


Review = get_model(app_name="review", model_name="Review")


@register(Review)
class ReviewAdmin(ModelAdmin):
    list_display = (
        "created",
        "reviewer",
        "reviewee",
        "performance_rating",
        "delivery_rating",
        "socialization_rating",
        "performance_comment",
        "delivery_comment",
        "socialization_comment",
        "modified",
    )
    list_filter = ("reviewer", "reviewee", "created")
    search_fields = ("reviewer__username", "reviewee__username")
    readonly_fields = ("modified",)
    ordering = ("-created",)
