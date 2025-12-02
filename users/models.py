from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from companies.models import Company
from .validators import validate_rut

class User(AbstractUser):
    ROLES = (
        ('super_admin', 'Super Admin'),
        ('admin_cliente', 'Admin Cliente'),
        ('gerente', 'Gerente'),
        ('vendedor', 'Vendedor'),
    )
    role = models.CharField(max_length=20, choices=ROLES)
    email = models.EmailField(unique=True)
    rut = models.CharField(max_length=12, unique=True, validators=[validate_rut])
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.username} ({self.role})"
