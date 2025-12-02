from django.core.exceptions import ValidationError
import re

def validate_rut(value):
    """
    RUT validator (Chile).
    """
    rut_pattern = re.compile(r'^0*(\d{1,3}(\.?\d{3})*)\-?([\dkK])$')
    match = rut_pattern.match(value)
    if not match:
        raise ValidationError('Invalid RUT format. Use 12.345.678-9 format.')

    rut_number, dv = match.group(1).replace('.', ''), match.group(3).lower()
    
    try:
        int_rut = int(rut_number)
    except ValueError:
        raise ValidationError('Invalid RUT number.')

    reversed_rut = str(int_rut)[::-1]
    factors = [2, 3, 4, 5, 6, 7, 2, 3]
    total = sum(int(digit) * factor for digit, factor in zip(reversed_rut, factors))
    
    remainder = total % 11
    expected_dv = str(11 - remainder)
    if expected_dv == '11':
        expected_dv = '0'
    elif expected_dv == '10':
        expected_dv = 'k'

    if dv != expected_dv:
        raise ValidationError('Invalid RUT digit.')
