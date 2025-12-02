from django.db import models
from companies.models import Company
from django.core.exceptions import ValidationError

class Subscription(models.Model):
    PLAN_CHOICES = (
        ('Basico', 'Básico'),
        ('Estandar', 'Estándar'),
        ('Premium', 'Premium'),
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=20, choices=PLAN_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)

    def clean(self):
        if self.end_date <= self.start_date:
            raise ValidationError('End date must be after start date.')

    def __str__(self):
        return f"{self.company.name} - {self.plan_name}"
