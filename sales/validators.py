from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_not_future_date(value):
    if value > timezone.now():
        raise ValidationError("The date cannot be in the future.")
