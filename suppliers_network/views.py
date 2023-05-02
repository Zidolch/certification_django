from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from suppliers_network.filters import NetworkObjectFilter
from suppliers_network.models import NetworkObject
from suppliers_network.permissions import IsActiveUser
from suppliers_network.setializers import NetworkObjectSerializer, NetworkObjectCreateSerializer


class NetworkObjectViewSet(viewsets.ModelViewSet):
    queryset = NetworkObject.objects.all()
    permission_classes = [IsActiveUser]
    filter_backends = [DjangoFilterBackend]
    filterset_class = NetworkObjectFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return NetworkObjectCreateSerializer
        else:
            return NetworkObjectSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.clean()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.clean()
