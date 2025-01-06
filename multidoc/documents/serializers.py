from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    organization = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Document
        fields = ['id', 'title', 'content', 'organization', 'created_by', 'created_at', 'updated_at']
        read_only_fields = ['created_by', 'created_at', 'updated_at', 'organization']