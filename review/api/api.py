from rest_framework.viewsets import ModelViewSet
from review.api.serializers import ReviewSerializer
from utils.utils import get_model

Review = get_model(app_name="review", model_name="Review")


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
