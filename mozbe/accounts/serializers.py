from __future__ import absolute_import

from rest_framework import serializers

from .models import Provider
from .models import PolygonArea


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class PolygonAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = PolygonArea
        fields = '__all__'






