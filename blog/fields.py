from django.db import models
from .validators import phone_number_validator, zipcode_validator, pre_zipcode_validator


class PhoneNumberField(models.CharField):
    def __init__(self, *args, **kwargs):
        # PhoneNumberField() --> models.CharField(max_length=20, validators=[phone_number_validator])
        kwargs.setdefault('max_length', 20)
        kwargs.setdefault('validators', [])
        kwargs['validators'].append(phone_number_validator)
        # kwargs['max_length'] = 20
        # kwargs['validators'] = phone_number_validator()
        # Error 리스트 타입으로 받아야 함.
        super().__init__(*args, **kwargs)


class ZipCodeField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 5
        kwargs['validators'] = [zipcode_validator]
        super().__init__(*args, **kwargs)


class PreZipCodeField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 7
        kwargs['validators'] = [pre_zipcode_validator]
        super().__init__(*args, **kwargs)


# # import csv(comma-separated-values)
# CSV_PATH = "path/filename.txt"
# reader = csv.reader(open(CSV_PATH, "rt", encoding="cp949"), delimiter="|")
# #     columns = next(reader)
# # # dict로 전한 후 우편번호 컬럼만 --> 존재하는 우편번호인지 검사할 때
# # for idx, row in enumerate(reader):
# #     data = dict(zip(columns, row))
#       if idx > 4:
#           break
# #     return data['우편번호']
