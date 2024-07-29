from django.contrib import admin
from .models import PurchaseOrder, Inventory, OutboundRequest

admin.site.register(PurchaseOrder)
admin.site.register(Inventory)
admin.site.register(OutboundRequest)
