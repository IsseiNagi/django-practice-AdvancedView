from django.core.exceptions import ValidationError
import re


class CustomPasswordValidator():

    def __init__(self):
        pass

    def validate(self, password, user=None):
        if all((
            # 以下の全ての条件をみたいしている場合にTrue
            re.search('[0-9]', password),
            re.search('[a-z]', password),
            re.search('[A-Z]', password),
        )):
            return
        raise ValidationError('パスワードには0-9, a-z, A-Zを含めてください')

    def get_help_text(self):
        return 'パスワードには0-9, a-z, A-Zを含めてください'
