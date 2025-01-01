from utils.utils import get_model
from rest_framework.serializers import (
    ModelSerializer,
    CurrentUserDefault,
    Serializer,
    FileField,
    ValidationError,
)
from users.api.serializers import RelatedUserSerializer
from markdown import markdown

BroadCast = get_model(app_name="quick_hr", model_name="BroadCast")
Holiday = get_model(app_name="quick_hr", model_name="Holiday")


class BroadCastSerializer(ModelSerializer):
    user = RelatedUserSerializer(default=CurrentUserDefault())

    class Meta:
        model = BroadCast
        fields = [
            "id",
            "title",
            "description",
            "user",
            "created_ago",
        ]
        read_only_fields = ["id"]

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        data["description"] = markdown(data["description"])
        return data


class HolidaySerializer(ModelSerializer):
    class Meta:
        model = Holiday
        fields = ["id", "title", "description", "starts_from", "ends_on", "no_of_days"]
        read_only_fields = ["id"]


class HolidayCsvSerializer(Serializer):
    csv = FileField()

    def validate(self, attrs):
        if attrs["csv"].name.split(".")[-1] != "csv":
            raise ValidationError("Invalid file type")
        return attrs

    def create(self, validated_data):
        """Create a DataFrame from the csv file & Create Holidays Data"""
        import pandas as pd

        df = pd.read_csv(validated_data["csv"])
        if not all(
            [
                col in df.columns
                for col in ["title", "description", "starts_from", "ends_on"]
            ]
        ):
            raise ValidationError("Invalid csv file")

        formatted_rows = []
        df["starts_from"] = pd.to_datetime(df["starts_from"]).dt.date
        df["ends_on"] = pd.to_datetime(df["ends_on"]).dt.date

        for _, row in df.iterrows():
            try:
                serializer = HolidaySerializer(data=row.to_dict())
                serializer.is_valid(raise_exception=True)
                formatted_rows.append(serializer.validated_data)
            except ValidationError as e:
                raise e
        Holiday.objects.bulk_create([Holiday(**data) for data in formatted_rows])
        return True
