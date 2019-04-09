'''
Generate a ten-character alphanumeric password.
'''
import secrets
import string
alphabets = string.ascii_letters + string.digits
password = "".join(secrets.choice(alphabets) for i in range(10))

print(password)
