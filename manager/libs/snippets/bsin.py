from django.core.validators import RegexValidator
import random
import string


class BSIN:

    BSINValidator = RegexValidator(r'^[1-9A-NP-Z]*$', 'Only uppercase \
        alphanumeric characters different from 0 and O are \
        allowed.')

    @staticmethod
    def generate_bsin():
        return "".join([random.choice(
            (string.ascii_uppercase + string.digits).translate(None, '0O'))
            for x in range(6)])

    @staticmethod
    def allowed_characters():
        (string.ascii_uppercase + string.digits).translate(None, '0O')
