from rest_framework import viewsets
from rest_framework.response import Response
from core.models import Organization, OrganizationMember
from core.serializers import OrganizationSerializer, OrganizationMemberSerializer
from rest_framework.decorators import action

class OrganizationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer
    
    def get_queryset(self):
        return Organization.objects.filter(
            organizationmember__user=self.request.user
        ).distinct()
    
    def perform_create(self, serializer):
        organization = serializer.save()
        # Create member entry for creator as admin
        OrganizationMember.objects.create(
            user=self.request.user,
            organization=organization,
            role='admin'
        )
        
    @action(detail=True, methods=['post'])
    def add_member(self, request, pk=None):
        organization = self.get_object()
        user_id = request.data.get('user_id')
        role = request.data.get('role')
        
        member = OrganizationMember.objects.create(
            user_id=user_id,
            organization=organization,
            role=role
        )
        
        return Response(
            OrganizationMemberSerializer(member).data,
            status=201
        )