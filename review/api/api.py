from rest_framework.viewsets import GenericViewSet
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from review.api.serializers import ReviewSerializer
from utils.utils import get_model
from django.db import IntegrityError
from rest_framework.response import Response
from utils.permissions import DepartmentManager
from django.db.models import Q
from rest_framework.decorators import action
from django.utils.timezone import now
from dateutil.relativedelta import relativedelta
from review.filters import ReviewFilter
from review.constants import AuthMessages

Review = get_model(app_name="review", model_name="Review")
User = get_model(app_name="users", model_name="User")


class ReviewViewSet(
    ListModelMixin, CreateModelMixin, DestroyModelMixin, GenericViewSet
):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filterset_class = ReviewFilter
    filterset_fields = ["status"]

    def get_permissions(self):
        if self.request.method == "POST":
            return [DepartmentManager()]
        return super().get_permissions()

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        query = Q(
            reviewee__employee__organization=self.request.user.employee.organization
        )
        if self.request.method == "POST":
            query = query & Q(
                reviewee__employee__department=self.request.user.employee.department
            )
        else:
            query = query & Q(reviewee=self.request.user)
        return queryset.filter(query).distinct()

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response(
                {"error": AuthMessages.REVIEW_ALREADY_EXISTS},
                status=HTTP_400_BAD_REQUEST,
            )

    @action(detail=False, methods=["get"])
    def recent_reviews(self, request, *args, **kwargs):
        """Returns 6 Months Recent Reviews Details"""
        queryset = self.filter_queryset(self.queryset).filter(
            created__gte=now() - relativedelta(months=6)
        )
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)
