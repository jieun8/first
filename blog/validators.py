import re
from django.forms import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible
import requests
import xmltodict
from django.conf import settings
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
    if not re.match(r'^01[016789][1-9]\d{6,7}$', value):
        raise ValidationError('다시 입력')


def zipcode_validator(value):
    if not re.match(r'^0[1-9]\d{3}$', str(value)) and not re.match(r'^[1-5]\d{4}$', str(value)) and not re.match(r'^6[0-3]\d{3}$', str(value)):
        raise ValidationError('우편번호 형식과 일치하지 않음')


def pre_zipcode_validator(value):
    if not re.match(r'^\d{3}-\d{3}$', str(value)):
        raise ValidationError('구 우편번호 형식과 일치하지 않음')


@deconstructible
class ZipCodeValidator(object):
    '우편번호 체계안내 : http://www.koreapost.go.kr/kpost/sub/subpage.jsp?contId=010101040100'

    def __init__(self, is_check_exist):
        self.is_check_exist = is_check_exist

    def __call__(self, zip_code):
        if not re.match(r'^\d{6}$', zip_code):
            raise ValidationError('6자리 숫자로 입력해주세요.')

        # if self.is_check_exist:
        from .models import ZipCode
        if not ZipCode.objects.filter(code=zip_code).exists():
            return ValidationError('x')
    #         self.check_exist_from_db(zip_code)
    #         # self.check_exist(zip_code)

    # def check_exist_from_db(self, zip_code):
    #     from .models import ZipCode
    #     if not ZipCode.objects.filter(code=zip_code).exists():
    #         return ValidationError('x')

    # DB 저장으로 대체ㄴㄴㄴㄴ
    def check_exist(self, zip_code):
        '우체국 open api : http://biz.epost.go.kr/customCenter/custom/custom_10.jsp'

        params = {
            'regkey': settings.EPOST_API_KEY,
            'target': 'postNew',
            'query': zip_code,
        }
        xml = requests.get('http://biz.epost.go.kr/KpostPortal/openapi', params=params).text
        # .get --> response object
        response = xmltodict.parse(xml)
        # xmltodict.parse(xml_input, encoding='utf-8', expat=expat, process_namespaces=False, namespace_separator=':', **kwargs)
        # Parse the given XML input and convert it into a dictionary.

        # xml_input can either be a string or a file-like object.
        try:
            error = response['error'] # response, error 둘다 dict
        except KeyError:
            pass
        else:
            raise ValidationError('[{error_code}] {message}'.format(**error))