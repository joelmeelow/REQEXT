from .models import PharmMessages
from rest_framework import serializers

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PharmMessages
        fields = ["conversation", "content", "created_by"]