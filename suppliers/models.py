from django.db import models
from users.validators import validate_rut

class Supplier(models.Model):
    name = models.CharField(max_length=150)
    rut = models.CharField(max_length=12, unique=True, validators=[validate_rut])
    contact = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name
