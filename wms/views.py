from django.shortcuts import render
from .models import PurchaseOrder, Inventory, OutboundRequest

def index(request):
    purchase_orders = PurchaseOrder.objects.all()
    inventories = Inventory.objects.all()
    outbound_requests = OutboundRequest.objects.all()
    context = {
        'purchase_orders': purchase_orders,
        'inventories': inventories,
        'outbound_requests': outbound_requests,
    }
    return render(request, 'wms/index.html', context)
