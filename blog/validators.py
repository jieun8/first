import re
from django.forms import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible
# migration에서는 wrap (x)

def lnglat_validator(value):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')



@deconstructible
class MinLengthValidator(object):
    def __init__(self, min_length):
        self.min_length = min_length
        # NoneType object is not callable

    def __call__(self, value):
        if len(value) < self.min_length:
            raise ValidationError('{}글자보다 많이쓰세요'.format(self.min_length))



@deconstructible
class MaxLengthValidator(object):
    def __init__(self, max_length):
        self.max_length = max_length

    def __call__(self, value):
        if len(value) > self.max_length:
            return ValidationError('{}글자보다 작게쓰세요'.format(self.max_length))



def phone_number_validator(value):
    if not re.match(r'^01[016789][1-9]\d{6, 7}$', value):
        raise ValidationError('다시 입력')