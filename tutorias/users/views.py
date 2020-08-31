from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from guardian.shortcuts import assign_perm

from permissions.services import APIPermissionClassFactory

from users.models import User
from users.serializers import UserSerializer

def is_self(user, obj, request):
    return user.email == obj.email


def vibe_check(user, obj, request):
    return False


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='ReaderPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                },
                'instance': {
                    'retrieve': False,
                    'destroy': False,
                    'update': False,
                    'get_info':True,
                }
            }
        ),
    )

    def perform_create(self, serializer):
        user = self.request.user
        user = serializer.save()
        return Response(serializer.data)

    @action(detail=True, methods=['POST'], url_path='info')
    def get_info(self, request, pk=None):
        user = self.get_object()
        info = get_object_or_404(User, email=user)
        serialized = UserSerializer(info).data
        return Response(serialized)
