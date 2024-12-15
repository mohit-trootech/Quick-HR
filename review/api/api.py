from rest_framework.viewsets import ModelViewSet
from review.api.serializers import ReviewSerializer
from utils.utils import get_model
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError

Review = get_model(app_name="review", model_name="Review")
User = get_model(app_name="users", model_name="User")


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    search_fields = ("reviewer__username", "reviewee__username")
    filterset_fields = ["status"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data["reviewee"] = User.objects.get(
            id=request.data.get("reviewee")
        )
        try:
            self.perform_create(serializer)
        except IntegrityError:
            pass
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
