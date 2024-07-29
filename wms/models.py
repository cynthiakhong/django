from django.db import models

class PurchaseOrder(models.Model):
    order_id = models.CharField(max_length=50)
    material = models.CharField(max_length=100)
    quantity_ordered = models.IntegerField()
    eta_date = models.DateField()

    def __str__(self):
        return self.order_id

class Inventory(models.Model):
    material = models.CharField(max_length=100)
    quantity = models.IntegerField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.material

class OutboundRequest(models.Model):
    request_id = models.CharField(max_length=50)
    material = models.CharField(max_length=100)
    quantity_requested = models.IntegerField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.request_id
