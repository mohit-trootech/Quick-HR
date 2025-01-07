from utils.utils import get_model
from rest_framework.serializers import (
    ModelSerializer,
    CurrentUserDefault,
    ValidationError,
    Serializer,
    IntegerField,
)
from utils.serailizers import RelatedUserSerializer, DynamicFieldsBaseSerializer
from review.constants import AuthMessages

Review = get_model(app_name="review", model_name="Review")
User = get_model(app_name="users", model_name="User")


class RevieweeReviewerSerializer(Serializer):
    reviewee = IntegerField(required=True)
    reviewer = IntegerField(required=True)

    def validate(self, attrs):
        reviewer = (
            User.objects.select_related("employee").get(id=attrs["reviewer"]).employee
        )
        reviewee = (
            User.objects.select_related("employee").get(id=attrs["reviewee"]).employee
        )
        # Check if ids of reviewer & reviewee are same
        if reviewer == reviewee:
            raise ValidationError(
                {"non_field_errors": [AuthMessages.REVIEWER_REVIEWEE_SAME]}
            )
        if reviewer.organization != reviewee.organization:
            raise ValidationError(
                {
                    "non_field_errors": [
                        AuthMessages.REVIEWER_REVIEWEE_DIFFERENT_ORGANIZATION
                    ]
                }
            )
        if reviewer.department != reviewee.department:
            raise ValidationError(
                {
                    "non_field_errors": [
                        AuthMessages.REVIEWER_REVIEWEE_DIFFERENT_DEPARTMENT
                    ]
                }
            )
        return super().validate(attrs)

    def validate_reviewee(self, value):
        try:
            User.objects.get(id=value)
            return value
        except User.DoesNotExist:
            raise ValidationError(AuthMessages.REVIEWEE_NOT_FOUND)

    def validate_reviewer(self, value):
        try:
            User.objects.get(id=value)
            return value
        except User.DoesNotExist:
            raise ValidationError(AuthMessages.REVIEWER_NOT_FOUND)


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
        serializer = RevieweeReviewerSerializer(
            data={
                "reviewer": self.context["request"].user.id,
                "reviewee": self.initial_data["reviewee"],
            }
        )
        serializer.is_valid(raise_exception=True)
        validated_data["reviewee"] = User.objects.get(
            id=serializer.validated_data["reviewee"]
        )
        return super().create(validated_data)
