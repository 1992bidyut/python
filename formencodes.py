import formencode
from formencode import validators
validator = validators.Int()
validator.to_python("10")
10
# validator.to_python("ten")
def valid_input(prompt, validator):
    while 1:
        try:
            value = input(prompt)
            return validator.to_python(value)
        except formencode.Invalid as e:
            print (e)
valid_input('Enter your email: ', validators.Email())