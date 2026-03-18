from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.username', read_only=True)
    last_updated_by_name = serializers.CharField(source='last_updated_by.username', read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'status', 'remarks', 'created_on', 'last_updated_on', 'created_by', 'last_updated_by', 'created_by_name', 'last_updated_by_name']
        read_only_fields = ['created_on', 'last_updated_on', 'created_by', 'last_updated_by']