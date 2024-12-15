from utils.utils import get_model
from rest_framework.serializers import ModelSerializer
from utils.serailizers import RelatedUserSerializer, DynamicFieldsBaseSerializer

Review = get_model(app_name="review", model_name="Review")


class ReviewSerializer(DynamicFieldsBaseSerializer, ModelSerializer):
    reviewer = RelatedUserSerializer(read_only=True)
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
            "reviewer",
            "reviewee",
            "status",
        )

    def create(self, validated_data):
        validated_data["reviewer"] = self.context["request"].user
        return super().create(validated_data)
