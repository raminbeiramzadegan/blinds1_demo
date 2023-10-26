from django.core.exceptions import ValidationError
import re

def validate_canadian_zip(value):
    pattern = r'^[A-Za-z]\d[A-Za-z][ -]?\d[A-Za-z]\d$'

    if not re.match(pattern, value):
        raise ValidationError('Invalid Canadian zip code. The format should be "ANA NAN."')
