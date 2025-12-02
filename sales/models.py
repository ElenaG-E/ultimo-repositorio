from django.db import models
from branches.models import Branch
from users.models import User
from products.models import Product
from django.utils import timezone
from .validators import validate_not_future_date

class Sale(models.Model):
    PAYMENT_CHOICES = (
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
    )
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    created_at = models.DateTimeField(default=timezone.now, validators=[validate_not_future_date])

    def __str__(self):
        return f"Venta {self.id} - {self.branch.name} - {self.total}"

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
