from .models import Task
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = 'id title description completed created'.split()


class TaskValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(required=False)
    completed = serializers.CharField()
    created = serializers.DateTimeField()
