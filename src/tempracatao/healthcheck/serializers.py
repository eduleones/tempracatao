from rest_framework import serializers

from tempracatao.healthcheck.enums import Status


class HealthcheckSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=Status.choices())
