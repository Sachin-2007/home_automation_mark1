import secrets
import string

def generate_code(length):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    code = '/' + ''.join(secrets.choice(chars) for i in range(0, length))
    return code
