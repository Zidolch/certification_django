import django_filters

from suppliers_network.models import NetworkObject


class NetworkObjectFilter(django_filters.FilterSet):
    country = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = NetworkObject
        fields = ['country']
