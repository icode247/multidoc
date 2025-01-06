from rest_framework import viewsets
from rest_framework.response import Response
from .models import Document
from .serializers import DocumentSerializer
from django.shortcuts import get_object_or_404
from core.models import Organization

class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    
    def get_queryset(self):
        """
        This gets overridden with Permit.io permission checks later
        """
        organization_id = self.request.headers.get('X-Organization-Id')
        if not organization_id:
            return Document.objects.none()
        return Document.objects.filter(organization_id=organization_id)

    def perform_create(self, serializer):
        """
        This gets overridden with Permit.io permission checks later
        """
        organization_id = self.request.headers.get('X-Organization-Id')
        organization = get_object_or_404(Organization, id=organization_id)
        serializer.save(
            organization=organization,
            created_by=self.request.user
        )

