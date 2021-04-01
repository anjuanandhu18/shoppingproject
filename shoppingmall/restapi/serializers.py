from rest_framework import serializers
from .models import apimodel


class ApiModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = apimodel
        fields = ['name', 'description', 'number']
