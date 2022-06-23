from typing import Any, List, Type

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from tempracatao import __version__


class IndexSerializer(serializers.Serializer):
    version = serializers.CharField()


class IndexView(APIView):
    authentication_classes: List[Any] = []
    permission_classes: List[Any] = []
    serializer_class: Type[IndexSerializer] = IndexSerializer

    def get(self, request, format=None):
        serializer = IndexSerializer(data={"version": __version__})
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data)
