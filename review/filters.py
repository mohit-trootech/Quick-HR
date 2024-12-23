from django_filters import filters
from utils.utils import get_model

Review = get_model(app_name="review", model_name="Review")


class ReviewFilter(filters.Filter):
    month = filters.NumberFilter(lookup_expr="month", field_name="created")
    year = filters.NumberFilter(lookup_expr="year", field_name="created")

    class Meta:
        model = Review
        fields = ["month", "year", "reviewer__username", "reviewee__username"]
