from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from suppliers_network.models import NetworkObject, Product


@admin.action(description='Очистить задолженность')
def nullify_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "model", "release_date")


@admin.register(NetworkObject)
class NetworkObjectAdmin(admin.ModelAdmin):
    list_display = ("name", 'supplier_link', 'debt')
    list_filter = ["city"]
    actions = [nullify_debt]

    def supplier_link(self, obj):
        url = reverse('admin:suppliers_network_networkobject_change', args=[obj.supplier_id])
        return format_html('<a href="{}">{}</a>', url, obj.supplier)

    supplier_link.short_description = 'Поставщик'

