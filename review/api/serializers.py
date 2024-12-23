from utils.utils import get_model
from rest_framework.serializers import (
    ModelSerializer,
    CurrentUserDefault,
    ValidationError,
)
from utils.serailizers import RelatedUserSerializer, DynamicFieldsBaseSerializer

Review = get_model(app_name="review", model_name="Review")


class ReviewSerializer(DynamicFieldsBaseSerializer, ModelSerializer):
    reviewer = RelatedUserSerializer(default=CurrentUserDefault())
    reviewee = RelatedUserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = (
            "id",
            "reviewer",
            "reviewee",
            "performance_rating",
            "performance_comment",
            "delivery_rating",
            "delivery_comment",
            "socialization_rating",
            "socialization_comment",
            "created",
            "modified",
            "overall_review",
            "status",
        )
        read_only_fields = (
            "id",
            "created",
            "modified",
            "overall_review",
            "status",
        )

    def create(self, validated_data):
        # TODO : Ask for Better Approch
        # Check if reviewer and reviewee are the same
        if validated_data["reviewer"] == validated_data["reviewee"]:
            raise ValidationError(
                {"non_field_errors": ["Reviewer and reviewee cannot be the same."]}
            )
        # Check if reviewer and reviewee are in same organization
        if (
            validated_data["reviewer"].employee.organization
            != validated_data["reviewee"].employee.organization
        ):
            raise ValidationError(
                {
                    "non_field_errors": [
                        "Reviewer and reviewee must be in the same organization."
                    ]
                }
            )
        # Check if reviewer and reviewee are in the same department
        if (
            validated_data["reviewer"].employee.department
            != validated_data["reviewee"].employee.department
        ):
            raise ValidationError(
                {
                    "non_field_errors": [
                        "Reviewer and reviewee must be in the same department."
                    ]
                }
            )
        return super().create(validated_data)

    def validate_performance_rating(self, value):
        if value < 1 or value > 5:
            raise ValidationError("Performance Rating must be between 1 and 5.")
        return value

    def validate_delivery_rating(self, value):
        if value < 1 or value > 5:
            raise ValidationError("Delivery Rating must be between 1 and 5.")
        return value

    def validate_socialization_rating(self, value):
        if value < 1 or value > 5:
            raise ValidationError("Socialization Rating must be between 1 and 5.")
        return value
